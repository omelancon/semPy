import ast
import collections
import copy
import itertools
import logging
import operator
import os
import types

from . import api


def get_unique_name(name="var", _unique_name_counter=itertools.count()):
    return f"{name}__{next(_unique_name_counter)}_"


# ======================================================================================================================
#  Preprocessing of AST
# ======================================================================================================================
def get_node_ppy_info(node, item):
    if hasattr(node, "_ppy"):
        return node._ppy.get(item)
    else:
        node._ppy = {}
        return None


def set_node_ppy_info(node, item, value):
    if hasattr(node, "_ppy"):
        node._ppy[item] = value
    else:
        node._ppy = {item: value}


class NameScopeResolver(ast.NodeVisitor):
    def __init__(self, fn, parent=None):
        self.fn = fn
        self.parent = parent
        self._locals = None
        self._queue = []

    def resolve(self):
        fn = self.fn
        scope_info = get_node_ppy_info(fn, "locals")

        if scope_info is not None:
            # Already resolved
            return
        else:
            set_node_ppy_info(fn, "locals",
                              set(a.arg for a in [*fn.args.args, *fn.args.posonlyargs, *fn.args.kwonlyargs]))

        for stmt in fn.body:
            self.visit(stmt)

        for nested_fn in self._queue:
            NameScopeResolver(nested_fn).resolve()

    def visit_FunctionDef(self, node):
        get_node_ppy_info(self.fn, "locals").add(node.name)
        self._queue.append(node)

    def visit_ClassDef(self, node):
        raise NotImplementedError

    def visit_NonLocal(self, node):
        raise NotImplementedError

    def visit_Global(self, node):
        raise NotImplementedError

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            get_node_ppy_info(self.fn, "locals").add(node.id)


class NameMangler(ast.NodeTransformer):
    def __init__(self, fn, parent=None, mangle_table=None):
        if not isinstance(fn, ast.FunctionDef):
            raise TypeError("NameMangler can only apply to FunctionDef")

        self.fn = fn
        NameScopeResolver(self.fn).resolve()

        if mangle_table:
            self.mangle_table = {}
            for name in get_node_ppy_info(self.fn, "locals"):
                predefined_mangle = mangle_table.get(name)
                self.mangle_table[name] = predefined_mangle or get_unique_name(name)
        else:
            self.mangle_table = {name: get_unique_name(name) for name in get_node_ppy_info(self.fn, "locals")}

        if parent:
            self.mangle_table = {**parent.mangle_table, **self.mangle_table}

    def mangle_name(self, name):
        return self.mangle_table.get(name, name)

    def mangle(self, fn_name=None):
        fn_copy = copy.deepcopy(self.fn)

        mangled_body = [self.visit(stmt) for stmt in fn_copy.body]

        arguments = fn_copy.args
        mangled_args = [ast.arg(self.mangle_name(a.arg)) for a in arguments.args]
        mangled_posonlyargs = [ast.arg(self.mangle_name(a.arg)) for a in arguments.posonlyargs]
        mangled_kwonlyargs = [ast.arg(self.mangle_name(a.arg)) for a in arguments.kwonlyargs]
        mangled_vararg = arguments.vararg and ast.arg(self.mangle_name(arguments.vararg))
        mangled_kwarg = arguments.kwarg and ast.arg(self.mangle_name(arguments.kwarg))

        if arguments.kw_defaults or arguments.defaults:
            pass  # TODO: do not ignore default values

        return ast.FunctionDef(
            fn_name or fn_copy.name,
            ast.arguments(
                mangled_posonlyargs,
                mangled_args,
                mangled_vararg,
                mangled_kwonlyargs,
                [],
                mangled_kwarg,
                []),
            mangled_body,
            fn_copy.decorator_list)

    def visit_FunctionDef(self, node):
        nested_mangler = NameMangler(node, parent=self)
        return nested_mangler.mangle(fn_name=self.mangle_name(node.name))

    def visit_Name(self, node):
        return ast.Name(self.mangle_name(node.id), node.ctx)


# ======================================================================================================================
#  Postprocessing of AST
# ======================================================================================================================

class PPYNodeTransformer(ast.NodeTransformer):
    def generic_visit(self, node):
        for field, old_value in ast.iter_fields(node):
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, (ast.AST, PPYObject)):
                        value = self.visit(value)
                        if value is None:
                            continue
                        elif not isinstance(value, (ast.AST, PPYObject)):
                            new_values.extend(value)
                            continue
                    new_values.append(value)
                old_value[:] = new_values
            elif isinstance(old_value, (ast.AST, PPYObject)):
                new_node = self.visit(old_value)
                if new_node is None:
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
        return node


class PPYNodeVisitor(ast.NodeVisitor):
    def generic_visit(self, node):
        """Called if no explicit visitor function exists for a node."""
        for field, value in ast.iter_fields(node):
            if isinstance(value, list):
                for item in value:
                    if isinstance(item, (ast.AST, PPYObject)):
                        self.visit(item)
            elif isinstance(value, (ast.AST, PPYObject)):
                self.visit(value)


def remove_extra_pass(behavior):
    body = behavior if isinstance(behavior, list) else behavior.body
    body[:] = [stmt for stmt in body if not isinstance(stmt, ast.Pass)] or [ast.Pass()]


class NameCounter(PPYNodeVisitor):
    def __init__(self, fn_or_body):
        self.fn_or_body = fn_or_body
        self.ref_counter = collections.Counter()
        self.assignments = collections.defaultdict(list)

    def apply(self):
        fn_or_body = self.fn_or_body
        body = fn_or_body if isinstance(fn_or_body, list) else fn_or_body.body

        for stmt in body:
            self.visit(stmt)

        return self.ref_counter, self.assignments

    def visit_FunctionDef(self, node):
        raise NotImplementedError("postprocessing does not expect nested function definitions")

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.ref_counter[node.id] += 1
        elif isinstance(node.ctx, ast.Store):
            raise NotImplementedError("NameCounter: ref with Store context out of assignment")
        else:
            raise NotImplementedError("assignment deletion")

    def visit_Assign(self, node):
        for t in node.targets:
            if isinstance(t, ast.Name):
                self.assignments[t.id].append(node.value)

    def visit_PPYValue(self, node):
        return node

    def visit_PPYConditional(self, node):
        return node

    def visit_PPYIntrinsic(self, node):
        return node

    def visit_PPYSingleton(self, node):
        return node


class DuplicateBranchingRemover(ast.NodeTransformer):
    # TODO this case is tricky...
    # When we inline a PPYConditional, it is often possible to remove its origin if-statement
    # Here we remove it in a very limited case which is when the PPYConditional is inlined in a return statement at the
    # end of the function body. Since we expect no side-effects this is safe, but could miss other cases
    # We can recognize the origin if-statement because it has the same condition object
    def __init__(self, fn_or_body):
        self.fn_or_body = fn_or_body
        self.ppy_conditional = None

    def apply(self):
        fn_or_body = self.fn_or_body
        body = fn_or_body if isinstance(fn_or_body, list) else fn_or_body.body
        last = body[-1]

        if isinstance(last, ast.Return):
            value = last.value
            if isinstance(value, PPYConditional):
                self.ppy_conditional = value

                new_body = [self.visit(s) for s in body]
                body[:] = [s for s in new_body if s is not None]

    def visit_If(self, node):
        if node.test is self.ppy_conditional.condition:
            return None
        else:
            return node


class DeadCodeRemover(ast.NodeTransformer):
    def __init__(self, node):
        self.node = node
        self._memo = set()

    def apply(self):
        return self.visit(self.node)

    def is_dead_end(self, stmt):
        if isinstance(stmt, ast.Return) or isinstance(stmt, ast.Raise):
            return True
        elif stmt in self._memo:
            return True
        elif isinstance(stmt, ast.If):
            if any(map(self.is_dead_end, stmt.body)) and any(map(self.is_dead_end, stmt.orelse)):
                self._memo.add(stmt)
                return True
        else:
            return False

    def remove_body_dead_code(self, body):
        new_body = []
        for stmt in body:
            new_body.append(stmt)
            if self.is_dead_end(stmt):
                break
        body[:] = new_body

    def remove_stmt_dead_code(self, node, fields=('body',)):
        for field in fields:
            self.remove_body_dead_code(getattr(node, field))

    def visit_FunctionDef(self, node):
        node = self.generic_visit(node)
        self.remove_stmt_dead_code(node)
        return node
    
    def visit_If(self, node):
        node = self.generic_visit(node)
        self.remove_stmt_dead_code(node, fields=('body', 'orelse'))
        return node



class AssignmentRemover(PPYNodeTransformer):
    def __init__(self, fn_or_body):
        self.fn_or_body = fn_or_body
        self.to_remove = set()
        self.to_inline = {}
        self.must_iterate = True
        self.ref_counter = self.assignments = None

    def apply(self):
        fn_or_body = self.fn_or_body
        body = fn_or_body if isinstance(fn_or_body, list) else fn_or_body.body

        while self.must_iterate:
            self.must_iterate = False
            ref_counter, assignments = self.ref_counter, self.assignments = NameCounter(fn_or_body).apply()

            # assignments which can be fully removed as they were inlined
            to_remove = self.to_remove
            for name, values in self.assignments.items():
                if ref_counter[name] == 0 and len(values) == 1:
                    to_remove.add(name)

            # assignments which can be inlined as the variable is single use
            for name, count in ref_counter.items():
                if count == 1:
                    name_assignments = assignments[name]
                    if len(name_assignments) == 1:
                        self.to_inline[name] = name_assignments[0].value

            new_body = [self.visit(s) for s in body]
            body[:] = [s for s in new_body if s is not None]

    def visit_Assign(self, node):
        if node.value is ppy_NotImplemented:
            return None # We know that semantically, all assignment to NotImplemented can be removed

        targets = node.targets
        new_targets = [t for t in targets if not isinstance(t, ast.Name) or t.id not in self.to_remove]

        if len(targets) != len(new_targets):
            self.must_iterate = True

        if new_targets:
            targets[:] = new_targets
            return node
        else:
            return None

    def visit_Name(self, node):
        res = self.to_inline.get(node.id, None)

        if res is None:
            return node
        else:
            self.must_iterate = True
            return res

    def visit_If(self, node):
        res = self.generic_visit(node)
        res_body = res.body
        res_orelse = res.orelse

        if not res_body and not res_orelse:
            return None
        elif not res_body:
            res_body.append(ast.Pass())
        elif not res_orelse:
            res_orelse.append(ast.Pass())

        return res

    def visit_PPYSingleton(self, node):
        return node

    def visit_PPYValue(self, node):
        return node

    def visit_PPYConditional(self, node):
        return node

    def visit_PPYIntrinsic(self, node):
        return node


class PPYValuesReplacer(PPYNodeTransformer):
    def __init__(self, fn_or_body):
        self.fn_or_body = fn_or_body

    def apply(self):
        fn_or_body = self.fn_or_body
        body = fn_or_body if isinstance(fn_or_body, list) else fn_or_body.body

        new_body = [self.visit(s) for s in body]
        body[:] = [s for s in new_body if s is not None]

    def visit_PPYValue(self, node):
        origin = node.origin
        if isinstance(origin, ast.arg):
            return ast.Name(origin.arg, ast.Load())
        elif node.origin:
            return self.generic_visit(origin)
        else:
            raise ValueError(f"Cannot replace {node} in ast")

    def visit_PPYIntrinsic(self, node):
        return ast.Name(node.name, ast.Load())

    def visit_PPYRaise(self, node):
        return ast.Raise(self.generic_visit(node.exception))

    def visit_PPYConditional(self, node):
        raise NotImplementedError

    def visit_PPYClass(self, node):
        return ast.Name(node.name, ast.Load())

    def visit_PPYSingleton(self, node):
        raise NotImplementedError # that should not happen unless we add singletons other than NotImplemented!

    def visit_Return(self, node):
        value = node.value
        if isinstance(value, PPYConditional):
            return ast.If(
                self.visit(value.condition),
                [self.visit(ast.Return(value.then_value))],
                [self.visit(ast.Return(value.orelse_value))])
        elif isinstance(value, PPYRaise):
            return self.visit_PPYRaise(value)
        else:
            return self.generic_visit(node)


# ======================================================================================================================
#  Data model for partially evaluated values
# ======================================================================================================================

class PPYObject:
    pass


# The PPY or ppy prefix means "partial python". Value prefixed with ppy are object from the partial evaluator runtime
class PPYValue(PPYObject):
    def __init__(self, *, origin, context, type=None, __type=type, **kwargs):
        super().__init__(**kwargs)
        self.origin = origin  # origin of the value in the ast
        self.context = context.copy() if context is not None else None  # copy of the context the value was computed in

        if type is not None:
            self.type = type
        elif isinstance(origin, ast.ClassDef):
            self.type = ppy_type_class
        elif isinstance(origin, ast.FunctionDef):
            self.type = ppy_function_class
        elif isinstance(origin, ast.Module):
            self.type = ppy_module_class
        elif isinstance(origin, ast.Compare):
            # In the context of behavior which are only for builtin types, a comparison will always return a bool
            self.type = ppy_bool_class
        elif isinstance(origin, ast.UnaryOp):
            if isinstance(origin.op, ast.Not):
                self.type = ppy_bool_class
            else:
                self.type = None
        elif isinstance(origin, ast.Call):
            self.type = self._resolve_call_return_type(origin)
        elif isinstance(origin, ast.Constant):
            self.type = type_name_to_ppy(__type(origin.value).__name__, context.modules)
        else:
            self.type = None

    def _resolve_call_return_type(self, call):
        func = call.func

        # Resolve return types of intrinsics functions
        if func in [ppy_intrinsic_py_int_from_host, ppy_intrinsic_py_float_to_int]:
            return ppy_int_class
        elif func is ppy_intrinsic_py_bool_from_host_bool:
            return ppy_bool_class
        elif func in [ppy_intrinsic_py_float_from_host, ppy_intrinsic_py_int_to_float]:
            return ppy_float_class
        elif func is ppy_intrinsic_py_str_from_host:
            return ppy_str_class

        return None

    @classmethod
    def with_type_only(cls, type):
        return cls(origin=None, context=None, type=type)


class PPYContainer(PPYObject):
    def __init__(self, *, items=None, **kwargs):
        super().__init__(**kwargs)
        self._items = items if items is not None else {}  # dict of attributes the container has after its evaluation

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, item, value):
        self._items[item] = value

    def __contains__(self, item):
        sentinel = object()
        return self.get(item, default=sentinel) is not sentinel

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            return default

    def items(self):
        return self._items.items()


class PPYSingleton(PPYValue):
    def __init__(self, *, name=None, origin=None, context=None, type=None, **kwargs):
        self.name = name
        super().__init__(origin=origin, context=context, type=type, **kwargs)


class PPYFunction(PPYValue):
    pass


class PPYClosure(PPYFunction):
    def __init__(self, *, context, **kwargs):
        super().__init__(context=context, **kwargs)
        self.parent_rte = context


class PPYSemantics(PPYFunction):
    pass


class PPYClass(PPYValue, PPYContainer):
    MRO_SELF_AND_OBJECT = object()
    MRO_SELF = object()

    def __init__(self, *, context, _mro=None, **kwargs):
        super().__init__(context=context, **kwargs)

        name = self.origin.name

        if _mro is PPYClass.MRO_SELF:
            self.mro = [self]
        elif _mro is PPYClass.MRO_SELF_AND_OBJECT:
            self.mro = [self, ppy_object_class]
        elif _mro is not None:
            self.mro = _mro
        else:
            # Use Python host types to determine mro
            klass = type_name_to_python(name)
            mro = klass.mro()

            ppy_mro = []

            for k in mro:
                kname = k.__name__

                if kname == name:
                    ppy_mro.append(self)
                else:
                    ppy_mro.append(type_name_to_ppy(kname, context.modules))

            self.mro = ppy_mro

        # Add __name__ to attributes as there is no support for descriptors yet
        self.name = name
        self["__name__"] = ast.Constant(name)


class PPYBaseModule(PPYContainer):
    pass


class PPYModule(PPYValue, PPYBaseModule):
    pass


class PPYStaticValue(PPYObject):
    _all = {}

    def __init__(self, name):
        self.name = name
        self._all[name] = self

    def __init_subclass__(cls, **kwargs):
        cls._all = {}


class PPYIntrinsic(PPYStaticValue):
    pass


class PPYBuiltin(PPYStaticValue):
    pass


class PPYRaise(PPYObject):
    def __init__(self, *, exception, context, **kwargs):
        super().__init__(**kwargs)
        self.exception = exception  # origin of the value in the ast
        self.context = context.copy() if context is not None else None  # copy of the context the value was computed in


class PPYConditional(PPYObject):
    def __init__(self, *, condition, then_value, orelse_value, identifier, **kwargs):
        super().__init__(**kwargs)
        self.condition = condition
        self.then_value = then_value
        self.orelse_value = orelse_value
        self.identifier = identifier


# ======================================================================================================================
#  Runtime Environment for partial evaluation
# ======================================================================================================================

class ReturnKind:
    def __init__(self, kind, info=None, rte=None, then=None, orelse=None):
        self.kind = kind
        self.info = info
        self.rte = rte
        self._then = then
        self._orelse = orelse

    @classmethod
    def as_return(cls):
        return cls("return")

    @classmethod
    def as_assign(cls, name, rte):
        return cls("assign", name, rte)

    @classmethod
    def as_expr(cls):
        return cls("expr")

    @classmethod
    def as_branch(cls, condition, rte):
        branch_return_kind = cls("branch", info=condition, rte=rte)
        then_return_kind = cls("then", info=branch_return_kind)
        orelse_return_kind = cls("orelse", info=branch_return_kind)

        branch_return_kind._then = then_return_kind
        branch_return_kind._orelse = orelse_return_kind

        return branch_return_kind

    @property
    def return_(self):
        return self.kind == "return"

    @property
    def assign(self):
        if self.kind == "assign":
            return self.info
        else:
            return False

    @property
    def expr(self):
        return self.kind == "expr"

    @property
    def then(self):
        return self.kind == "then"

    @property
    def orelse(self):
        return self.kind == "orelse"

    def do_return(self, value):
        if self.return_:
            return ast.Return(value)
        elif name := self.assign:
            self.rte[name] = value
            return ast.Assign([ast.Name(name, ast.Store())], value)
        elif self.expr:
            return value
        elif self.then or self.orelse:
            return self._do_branch_return(value)
        else:
            raise ValueError("wrong return kind")

    def _do_branch_return(self, value):
        conditional_return_kind = self.info
        parent_return_kind = conditional_return_kind.rte.return_kind

        if name := parent_return_kind.assign:
            rte = parent_return_kind.rte
            if self.then:
                previous_value = rte.get(name)
                rte[name] = PPYConditional(condition=conditional_return_kind.info,
                                           then_value=value,
                                           orelse_value=previous_value,
                                           identifier=conditional_return_kind)
                return ast.Assign([ast.Name(name, ast.Store())], value)
            elif self.orelse:
                previous_value = rte.get(name)
                if isinstance(previous_value, PPYConditional) and previous_value.identifier is conditional_return_kind:
                    previous_value.orelse_value = value
                else:
                    rte[name] = PPYConditional(condition=conditional_return_kind.info,
                                               then_value=previous_value,
                                               orelse_value=value,
                                               identifier=conditional_return_kind)
                return ast.Assign([ast.Name(name, ast.Store())], value)
        return parent_return_kind.do_return(value)

    def do_raise(self, exc):
        if self.then or self.orelse:
            return self._do_branch_raise(exc)
        else:
            return ast.Raise(exc)

    def _do_branch_raise(self, exc):
        conditional_return_kind = self.info
        parent_return_kind = conditional_return_kind.rte.return_kind

        if name := parent_return_kind.assign:
            rte = parent_return_kind.rte
            if self.then:
                previous_value = rte.get(name)
                rte[name] = PPYConditional(condition=conditional_return_kind.info,
                                           # TODO: if ever needed we could link ReturnKind to the context
                                           then_value=PPYRaise(exception=exc, context=None),
                                           orelse_value=previous_value,
                                           identifier=conditional_return_kind)
            elif self.orelse:
                previous_value = rte.get(name)
                if isinstance(previous_value, PPYConditional) and previous_value.identifier is conditional_return_kind:
                    previous_value.orelse_value = PPYRaise(exception=exc, context=None)
                else:
                    rte[name] = PPYConditional(condition=conditional_return_kind.info,
                                               then_value=previous_value,
                                               orelse_value=PPYRaise(exception=exc, context=None),
                                               identifier=conditional_return_kind)

        return ast.Raise(exc)


class RTE:
    def __init__(self, modules, globals=None, locals=None, closure=None, return_kind=ReturnKind.as_return()):
        self.modules = modules
        self._locals = locals
        self._closure = closure
        self._globals = globals
        self.return_kind = return_kind

    def __getitem__(self, item):
        val = self._locals and self._locals.get(item) \
              or self._closure and self._closure.get(item) \
              or self._globals.get(item)
        if val:
            return val
        else:
            ppy_builtins = self.modules["builtins"]
            val = ppy_builtins[item]

            if val:
                return val
            else:
                raise KeyError(item)

    def __setitem__(self, item, value):
        if self._locals is not None:
            self._locals[item] = value
        else:
            self._globals[item] = value

    def __contains__(self, item):
        sentinel = object()
        return self.get(item, default=sentinel) is not sentinel

    def get(self, item, default=None):
        try:
            return self[item]
        except KeyError:
            return default

    def copy(self):
        return RTE(self.modules,
                   globals=copy.copy(self._globals),
                   closure=copy.copy(self._closure),
                   locals=copy.copy(self._locals))

    def is_global(self):
        return self._locals is None

    def make_frame(self, closure=None, return_kind=ReturnKind.as_return()):
        return RTE(self.modules,
                   globals=self._globals,
                   locals={},
                   closure=closure,
                   return_kind=return_kind)

    def branch(self, condition):
        conditional_return_kind = ReturnKind.as_branch(condition, self)

        return RTE(self.modules,
                   globals=self._globals,
                   closure=self._closure,
                   locals=self._locals.copy(),
                   return_kind=conditional_return_kind._then), \
               RTE(self.modules,
                   globals=self._globals,
                   closure=self._closure,
                   locals=self._locals.copy(),
                   return_kind=conditional_return_kind._orelse)

    def merge(self, condition, then_rte, orelse_rte):
        then_locals = then_rte._locals
        orelse_locals = orelse_rte._locals

        for item in {*then_locals, *orelse_locals}:
            if then_locals.get(item) is not orelse_locals.get(item):
                raise NotImplementedError


# ======================================================================================================================
#  Mock module for __compiler_intrinsics__
# ======================================================================================================================

ppy_intrinsic_absent = PPYIntrinsic("absent")
ppy_intrinsic_sint = PPYIntrinsic("sint")
ppy_intrinsic_bint = PPYIntrinsic("bint")
ppy_intrinsic_class_getattr = PPYIntrinsic("class_getattr")
ppy_intrinsic_mro_lookup = PPYIntrinsic("mro_lookup")
ppy_intrinsic_define_semantics = PPYIntrinsic("define_semantics")
ppy_intrinsic_builtin = PPYIntrinsic("builtin")
ppy_intrinsic_private = PPYIntrinsic("private")
ppy_intrinsic_alloc = PPYIntrinsic("alloc")
ppy_intrinsic_py_int_from_host = PPYIntrinsic("py_int_from_host")
ppy_intrinsic_py_int_to_host = PPYIntrinsic("py_int_to_host")
ppy_intrinsic_py_float_from_host = PPYIntrinsic("py_float_from_host")
ppy_intrinsic_py_float_to_host = PPYIntrinsic("py_float_to_host")
ppy_intrinsic_py_bool_from_host_bool = PPYIntrinsic("py_bool_from_host_bool")
ppy_intrinsic_py_bool_to_host_bool = PPYIntrinsic("py_bool_to_host_bool")
ppy_intrinsic_py_str_to_host = PPYIntrinsic("py_str_to_host")
ppy_intrinsic_py_str_from_host = PPYIntrinsic("py_str_from_host")
ppy_intrinsic_py_str_len_to_host = PPYIntrinsic("py_str_len_to_host")
ppy_intrinsic_py_int_to_float = PPYIntrinsic("py_int_to_float")
ppy_intrinsic_py_float_to_int = PPYIntrinsic("py_float_to_int")

# do not make a copy of '_all', semantics are later loaded in intrinsics
ppy__compiler_intrinsics__ = PPYBaseModule(items=PPYIntrinsic._all)


# ======================================================================================================================
#  Evaluation of function specialization
# ======================================================================================================================

def partial_eval_function_call(fn, args, keywords, rte, return_kind=ReturnKind.as_return(), toplevel=False):
    # TODO: keywords is only passed to intrinsic_call to support the alloc intrinsic, extend it to other cases
    if isinstance(fn, PPYIntrinsic):
        yield from partial_eval_intrinsic_call(fn, args, keywords, rte, return_kind=return_kind)
    elif isinstance(fn, PPYBuiltin):
        yield from partial_eval_builtin_call(fn, args, rte, return_kind=return_kind)
    else:
        fn_origin = fn.origin

        if isinstance(fn_origin, ast.ClassDef):
            # Special case to skip partial evaluation of an exception instantiation
            try:
                klass = eval(fn_origin.name)
                if issubclass(klass, BaseException):
                    yield ast.Call(ast.Name(klass.__name__, ast.Load()), args, [])
                    return
            except NameError:
                raise TypeError(f"Calling non instantiable ppy class: {fn_origin.name}")

        fn_origin_args = fn_origin.args
        fn_origin_positional_args = fn_origin_args.posonlyargs + fn_origin_args.args

        if fn_origin_args.kwonlyargs or fn_origin_args.kw_defaults:
            raise NotImplementedError("partial_eval only supports positional arguments")

        arity = len(fn_origin_positional_args)
        if len(args) != arity:
            raise TypeError(
                f"partially evaluated function takes {arity} context arguments, {len(args)} were given.")

        if isinstance(fn, PPYClosure):
            call_rte = rte.make_frame(closure=fn.parent_rte, return_kind=return_kind)
        else:
            call_rte = rte.make_frame(return_kind=return_kind)

        # Apply name mangling for sound inlining
        mangle_table = {}
        for fn_arg, callee_arg in zip(fn_origin_positional_args, args):
            if isinstance(callee_arg, ast.AST):
                continue

            callee_arg_origin = callee_arg.origin

            if isinstance(callee_arg_origin, ast.Name):
                mangle_table[fn_arg.arg] = callee_arg_origin.id
            elif isinstance(callee_arg_origin, ast.arg):
                mangle_table[fn_arg.arg] = callee_arg_origin.arg

        if toplevel:
            for a in fn_origin_positional_args:
                mangle_table[a.arg] = a.arg

        mangled_fn_origin = NameMangler(fn.origin, mangle_table=mangle_table).mangle()

        mangled_ast_args = mangled_fn_origin.args

        fn_args = mangled_ast_args.posonlyargs + mangled_ast_args.args

        for fn_arg, callee_arg in zip(fn_args, args):
            if toplevel:
                callee_arg.origin = fn_arg
            call_rte[fn_arg.arg] = callee_arg

        yield from partial_eval_stmts(mangled_fn_origin.body, call_rte)


intrinsics_inverses = {
    (ppy_intrinsic_py_int_from_host, ppy_intrinsic_py_int_to_host),
    (ppy_intrinsic_py_float_from_host, ppy_intrinsic_py_float_to_host),
    (ppy_intrinsic_py_bool_to_host_bool, ppy_intrinsic_py_bool_from_host_bool),
    (ppy_intrinsic_py_str_to_host, ppy_intrinsic_py_str_from_host)
}

intrinsics_inverses = {
    *intrinsics_inverses,
    *map(lambda t: t[::-1], intrinsics_inverses)
}


def maybe_simplify_intrinsic_call(node, rte):
    if isinstance(node, ast.Call):
        return simplify_intrinsic_call(node.func, node.args, node.keywords, rte)
    else:
        return node


def simplify_intrinsic_call(fn, args, keywords, rte):
    if len(args) == 1 and not keywords:
        arg0 = args[0]

        if isinstance(arg0, PPYValue):
            arg0 = arg0.origin

        if isinstance(arg0, ast.Call) and len(arg0.args) == 1:
            right_fn = arg0.func

            if (fn, right_fn) in intrinsics_inverses:
                a = arg0.args[0]
                if right_fn is ppy_intrinsic_py_int_to_host:
                    # Check that the argument is indeed an int and not a bool
                    # in which case intrinsics apply down casting
                    if is_always_python_int(a, rte):
                        return maybe_simplify_intrinsic_call(a, rte)
                else:
                    return maybe_simplify_intrinsic_call(a, rte)

    return ast.Call(fn, args, keywords)


def partial_eval_intrinsic_call(fn, args, keywords, rte, return_kind=ReturnKind.as_return()):
    if fn is ppy_intrinsic_class_getattr:
        yield return_kind.do_return(intrinsic_eval_class_getattr_call(args, rte))
    elif fn is ppy_intrinsic_mro_lookup:
        yield return_kind.do_return(intrinsic_eval_mro_lookup_call(args, rte))
    elif isinstance(fn, PPYIntrinsic):
        # Cannot evaluate but can simplify
        value = simplify_intrinsic_call(fn, args, keywords, rte)
        if isinstance(value, PPYValue):
            yield return_kind.do_return(value)
        else:
            yield return_kind.do_return(PPYValue(origin=value, context=rte))
    else:
        raise NotImplementedError


# Evaluation of intrinsic calls
def intrinsic_eval_class_getattr_call(args, rte):
    # Assume correct arity
    obj = args[0]
    attr = args[1]

    if isinstance(obj, PPYValue):
        if isinstance(attr, ast.Constant) and isinstance(attr.value, str):
            type_ = obj.type

            if type_ is None:
                raise NotImplementedError(f"partial_eval_class_getattr_call: could not resolve type")

            return intrinsic_eval_mro_lookup_call([type_, attr], rte)
    else:
        raise NotImplementedError(
            "partial_eval_class_getattr_call: first argument must have been resolved to a ppy object")


def intrinsic_eval_mro_lookup_call(args, rte):
    type_ = args[0]
    attr = args[1]

    type_ = rte.modules["builtins"]["int"] if type_ in (ppy_intrinsic_sint, ppy_intrinsic_bint) else type_

    if not isinstance(type_, PPYClass):
        raise TypeError('intrinsic_eval_mro_lookup_call: first argument is not a type')

    if not isinstance(attr, ast.Constant) or not isinstance(attr.value, str):
        raise TypeError("intrinsic_eval_mro_lookup_call: second argument must be a string literal")

    attr_name = attr.value

    for ppy_class in type_.mro:
        attr = ppy_class.get(attr_name)

        if attr is not None:
            return attr

    return ppy_intrinsic_absent

# End of intrinsic calls

def partial_eval_builtin_call(fn, args, rte, return_kind=ReturnKind.as_return()):
    if fn is ppy_isinstance:
        yield return_kind.do_return(builtin_eval_isinstance_call(args, rte))
    elif fn is ppy_issubclass:
        yield return_kind.do_return(builtin_eval_issubclass_call(args, rte))
    elif fn is ppy_type:
        yield return_kind.do_return(builtin_eval_type_call(args, rte))
    else:
        raise NotImplementedError


# Evaluation of builtin calls
def builtin_eval_type_call(args, rte):
    # Assume correct arity
    instance, = args
    if isinstance(instance, PPYValue):
        instance_type = instance.type

        if isinstance(instance_type, PPYClass):
            return instance_type
        elif instance_type in (ppy_intrinsic_sint, ppy_intrinsic_bint):
            return ppy_int_class
        else:
            raise NotImplementedError
    elif isinstance(instance, ast.Compare):
        return ppy_bool_class
    elif isinstance(instance, ast.Constant):
        type_name = type(instance.value).__name__
        return type_name_to_ppy(type_name, rte.modules)
    else:
        raise NotImplementedError


def builtin_eval_isinstance_call(args, rte):
    # Assume correct arity
    instance, type_info = args

    type_info = ppy_type_class if type_info is ppy_type else type_info

    instance_type = instance.type

    if isinstance(type_info, PPYClass):
        if instance_type in (ppy_intrinsic_sint, ppy_intrinsic_bint):
            return ast.Constant(type_info is ppy_int_class)
        else:
            return ast.Constant(type_info in instance_type.mro)

    elif type_info is ppy_intrinsic_sint:
        return ast.Constant(instance_type in (ppy_intrinsic_sint, ppy_int_class))
    elif type_info is ppy_intrinsic_bint:
        return ast.Constant(instance_type in (ppy_intrinsic_bint, ppy_int_class))
    else:
        raise NotImplementedError


def builtin_eval_issubclass_call(args, rte):
    cls, type_info = args

    type_info = ppy_type_class if type_info is ppy_type else type_info

    if isinstance(type_info, PPYClass):
        if cls in (ppy_intrinsic_sint, ppy_intrinsic_bint):
            return ast.Constant(type_info is ppy_int_class)
        else:
            return ast.Constant(type_info in cls.mro)
    else:
        raise NotImplementedError


# End of builtin calls


def partial_eval_stmts(stmts, rte):
    for stmt in stmts:
        for evaluated_stmt in partial_eval_stmt(stmt, rte):
            yield evaluated_stmt
            if isinstance(evaluated_stmt, ast.Return) or isinstance(evaluated_stmt, ast.Raise):
                break


def partial_eval_stmt(stmt, rte):
    if isinstance(stmt, ast.If):
        yield from partial_eval_if(stmt, rte)
    elif isinstance(stmt, ast.Return):
        yield from partial_eval_return(stmt, rte)
    elif isinstance(stmt, ast.FunctionDef):
        partial_eval_def(stmt, rte)
        yield ast.Pass()  # in the context of behavior we do not consider functions as first class
    elif isinstance(stmt, ast.Assign):
        yield from partial_eval_assign(stmt, rte)
    elif isinstance(stmt, ast.Raise):
        yield rte.return_kind.do_raise(partial_eval_expr(stmt.exc, rte))
    else:
        raise NotImplementedError


def partial_eval_return(stmt, rte):
    value = stmt.value

    if isinstance(value, ast.Call):
        yield from partial_eval_return_tail_call(value, rte)
    else:
        ppy_expr = partial_eval_expr(value, rte)
        yield rte.return_kind.do_return(ppy_expr)


def partial_eval_expr_call(call, rte):
    func = call.func
    args = [partial_eval_expr(a, rte) for a in call.args]
    keywords = call.keywords
    if isinstance(func, ast.Name):
        name = func.id
        ppy_func = rte[name]
        yield from partial_eval_function_call(ppy_func, args, keywords, rte, return_kind=ReturnKind.as_expr())
    else:
        yield ast.Call(func, args, keywords)


def partial_eval_return_tail_call(call, rte):
    func = call.func
    args = [partial_eval_expr(a, rte) for a in call.args]
    keywords = call.keywords
    if isinstance(func, ast.Name):
        name = func.id
        ppy_func = rte[name]
        yield from partial_eval_function_call(ppy_func, args, keywords, rte, return_kind=rte.return_kind)
    else:
        yield rte.return_kind.do_return(ast.Call(func, args, keywords))


def partial_eval_assign_call(name, call, rte):
    func = call.func
    args = [partial_eval_expr(a, rte) for a in call.args]
    keywords = call.keywords
    if isinstance(func, ast.Name):
        func_name = func.id
        ppy_func = rte[func_name]
        yield from partial_eval_function_call(ppy_func, args, keywords, rte,
                                              return_kind=ReturnKind.as_assign(name, rte))
    else:
        yield ast.Assign([ast.Name(name, ast.Store())], ast.Call(func, args, keywords))


def partial_eval_assign(assign, rte):
    if len(assign.targets) == 1 and isinstance(assign.targets[0], ast.Name):
        name = assign.targets[0].id
        value = assign.value
        if isinstance(value, ast.Call):
            yield from partial_eval_assign_call(name, value, rte)
        else:
            ppy_value = partial_eval_expr(value, rte)
            rte[name] = PPYValue(origin=ppy_value, context=rte)
            yield ast.Assign(assign.targets, ppy_value)
    else:
        raise NotImplementedError("Unsupported assignment to multiple targets or non name targets")


def partial_eval_if(stmt, rte):
    test_result = partial_eval_expr(stmt.test, rte)
    maybe_host_bool = get_host_bool(test_result)

    if isinstance(test_result, ast.Constant):
        if test_result.value:
            yield from partial_eval_stmts(stmt.body, rte)
        else:
            yield from partial_eval_stmts(stmt.orelse, rte)
    elif maybe_host_bool is not None:
        if maybe_host_bool:
            yield from partial_eval_stmts(stmt.body, rte)
        else:
            yield from partial_eval_stmts(stmt.orelse, rte)
    else:
        then_rte, orelse_rte = rte.branch(test_result)

        then_body = list(partial_eval_stmts(stmt.body, then_rte))
        orelse_body = list(partial_eval_stmts(stmt.orelse, orelse_rte))

        rte.merge(test_result, then_rte, orelse_rte)

        yield ast.If(test_result, then_body, orelse_body)


def partial_eval_name(name, rte):
    return rte[name.id]


def partial_eval_expr(expr, rte):
    if isinstance(expr, ast.Call):
        resolved_call = list(partial_eval_expr_call(expr, rte))
        if len(resolved_call) != 1:
            remove_extra_pass(resolved_call)
            AssignmentRemover(resolved_call).apply()
            DuplicateBranchingRemover(resolved_call).apply()

        # List len should have changed if it was too long
        if len(resolved_call) == 1:
            return resolved_call[0]
        else:
            raise NotImplementedError
    elif isinstance(expr, ast.Name):
        return partial_eval_name(expr, rte)
    elif isinstance(expr, ast.Compare):
        return partial_eval_compare(expr, rte)
    elif isinstance(expr, ast.BoolOp):
        return partial_eval_bool_op(expr, rte)
    elif isinstance(expr, ast.BinOp):
        return partial_eval_bin_op(expr, rte)
    elif isinstance(expr, ast.UnaryOp):
        return partial_eval_un_op(expr, rte)
    elif isinstance(expr, ast.Attribute):
        raise NotImplementedError
    else:
        return expr


def partial_eval_un_op(expr, ctx):
    operand = partial_eval_expr(expr.operand, ctx)
    return ast.UnaryOp(expr.op, operand)


def get_operator_from_ast(op):
    return {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
    }.get(type(op))


def partial_eval_bin_op(expr, ctx):
    left = partial_eval_expr(expr.left, ctx)
    right = partial_eval_expr(expr.right, ctx)
    op = expr.op
    operator_ = get_operator_from_ast(op)

    if isinstance(left, ast.Constant) and isinstance(right, ast.Constant) and operator_:
        return ast.Constant(operator_(left.value, right.value))

    return ast.BinOp(left, op, right)


def partial_eval_bool_op(expr, ctx):
    op = expr.op
    values = [partial_eval_expr(e, ctx) for e in expr.values]

    evaluated_values = []

    # TODO: this is not exactly correct. For example, 'foo or True' will return foo even if foo is falsy.
    # TODO: this is ok for the current usage of partial evaluation, but could be improved once we have some time
    if isinstance(op, ast.And):
        for val in values:
            if isinstance(val, ast.Constant):
                if not val.value:
                    return val
            else:
                evaluated_values.append(val)

    elif isinstance(op, ast.Or):
        for val in values:
            if isinstance(val, ast.Constant):
                if val.value:
                    return val
            else:
                evaluated_values.append(val)
    else:
        raise NotImplementedError(f"missing partial_eval implementation for {type(op).__name__}")

    if not evaluated_values:
        # All values were evaluated, return the last one
        return val
    elif len(evaluated_values) == 1:
        return evaluated_values[0]
    else:
        return ast.BoolOp(op, evaluated_values)


def partial_eval_compare(cmp, rte):
    left = partial_eval_expr(cmp.left, rte)

    if len(cmp.comparators) > 1:
        raise NotImplementedError("partial_eval_compare: chain comparison not supported")
    else:
        op = cmp.ops[0]
        right = partial_eval_expr(cmp.comparators[0], rte)

        if isinstance(op, ast.Is):
            res = partial_eval_is(left, right, rte)
        elif isinstance(op, ast.IsNot):
            res = partial_eval_is_not(left, right, rte)
        elif isinstance(op, ast.Eq):
            res = partial_eval_eq(left, right, rte)
        elif isinstance(op, ast.NotEq):
            res = partial_eval_ne(left, right, rte)
        elif isinstance(op, ast.Lt):
            res = partial_eval_lt(left, right, rte)
        elif isinstance(op, ast.LtE):
            res = partial_eval_le(left, right, rte)
        elif isinstance(op, ast.Gt):
            res = partial_eval_gt(left, right, rte)
        elif isinstance(op, ast.GtE):
            res = partial_eval_ge(left, right, rte)
        else:
            res = None

        if res is None:
            return ast.Compare(left, [op], [right])
        else:
            return res


def is_chained_calls(node, names):
    if names:
        if isinstance(node, PPYValue):
            node = node.origin

        if isinstance(node, ast.Call) and node.func is names[0]:
            if len(node.args) == 1:
                return is_chained_calls(node.args[0], names[1:])
        return False
    else:
        return True


def resolve_expression_sign(expr, rte):
    if isinstance(expr, PPYValue) or isinstance(expr, ast.Call):
        if is_chained_calls(expr, [ppy_intrinsic_py_int_from_host, ppy_intrinsic_py_str_len_to_host]):
            return 1, False
    return None, None


# We implemented limited mechanism to detect whether a value is positive or negative
# This is mainly aimed at resolving the sign of int values coming from length of a sequence
def partial_eval_lt(left, right, rte):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, rte)

        if sign is not None:
            if sign == -1:
                if strict:
                    return ast.Constant(True)
            else:  # 0 or 1
                return ast.Constant(False)

    return None


def partial_eval_le(left, right, rte):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, rte)

        if sign is not None:
            if sign == -1 or sign == 0:
                return ast.Constant(True)

            elif strict:  # > 0
                return ast.Constant(False)

    return None


def partial_eval_gt(left, right, rte):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, rte)

        if sign is not None:
            if sign == 1:
                if strict:
                    return ast.Constant(True)
            else:  # 0 or -1
                return ast.Constant(False)

    return None


def partial_eval_ge(left, right, rte):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, rte)

        if sign is not None:
            if sign == 1 or sign == 0:
                return ast.Constant(True)

            elif strict:  # > 0
                return ast.Constant(False)

    return None


def is_always_python_numeric(expr, value, rte):
    if isinstance(expr, ast.Constant):
        return expr.value == value
    elif isinstance(expr, PPYValue):
        origin = expr.origin

        if isinstance(origin, ast.Constant):
            return is_always_python_numeric(origin, value, rte)
        elif isinstance(origin, ast.Call):
            return origin.func in (ppy_intrinsic_py_int_from_host,
                                   ppy_intrinsic_py_float_from_host,) \
                   and is_always_host_numeric(origin.args[0], value, rte)
    return False


def is_always_host_numeric(expr, value, rte):
    if isinstance(expr, PPYValue):
        origin = expr.origin

        if isinstance(origin, ast.Call):
            return origin.func in (ppy_intrinsic_py_int_to_host,
                                   ppy_intrinsic_py_float_to_host) \
                   and is_always_python_numeric(origin.args[0], value, rte)
    return False


def is_always_python_bint(expr, rte):
    if isinstance(expr, PPYValue):
        if expr.type is ppy_intrinsic_bint:
            return True
        origin = expr.origin

        if isinstance(origin, ast.Call) and origin.func is ppy_intrinsic_py_int_from_host:
            return is_always_host_bint(origin.args[0], rte)
    return False


def is_always_host_bint(expr, rte):
    if isinstance(expr, PPYValue):
        if expr.type is ppy_intrinsic_bint:
            return True
        origin = expr.origin

        if isinstance(origin, ast.Call) and origin.func is ppy_intrinsic_py_int_to_host:
            return is_always_python_bint(origin.args[0], rte)
    return False


def is_always_python_int(expr, rte):
    if isinstance(expr, PPYValue):
        if expr.type in (ppy_intrinsic_bint, ppy_intrinsic_sint, ppy_int_class):
            return True
        origin = expr.origin

        if isinstance(origin, ast.Call) and origin.func is ppy_intrinsic_py_int_from_host:
            return True
    return False


def is_always_host_int(expr, rte):
    if isinstance(expr, PPYValue):
        if expr.type is ppy_intrinsic_bint:
            return True
        origin = expr.origin

        if isinstance(origin, ast.Call) and origin.func is ppy_intrinsic_py_int_to_host:
            return True
    return False


def host_bool(b):
    return ast.Call(ppy_intrinsic_py_bool_to_host_bool, [ast.Constant(b)], [])


def get_host_bool(expr):
    if isinstance(expr, PPYValue):
        expr = expr.origin

    if isinstance(expr, ast.Call) and expr.func is ppy_intrinsic_py_bool_to_host_bool:
        if isinstance(arg0 := expr.args[0], ast.Constant):
            return arg0.value
    return None


def partial_eval_eq_left_bool(left, right, rte):
    if isinstance(right, ast.Constant):
        if right.value == 0:
            return ast.Compare(left, [ast.Is()], [ast.Constant(False)])
        elif right.value == 1:
            return ast.Compare(left, [ast.Is()], [ast.Constant(True)])
        else:
            return ast.Constant(False)
    elif isinstance(right, PPYValue):
        return partial_eval_eq_left_bool(left, right.origin, rte)
    else:
        return None


def is_always_python_bool(expr, rte):
    return isinstance(expr, PPYValue) and expr.type is ppy_bool_class \
           or isinstance(expr, ast.Constant) and isinstance(expr.value, bool)


def is_always_host_int_from_bool(expr, rte):
    if isinstance(expr, PPYValue):
        return is_always_host_int_from_bool(expr.origin, rte)
    else:
        return isinstance(expr, ast.Call) \
               and expr.func is ppy_intrinsic_py_int_to_host \
               and is_always_python_bool(expr.args[0], rte)


def partial_eval_eq_left_host_int_from_bool(left, right, rte):
    if isinstance(left, PPYValue):
        return partial_eval_eq_left_host_int_from_bool(left.origin, right, rte)
    if is_always_host_numeric(right, 0, rte):
        return ast.Call(ppy_intrinsic_py_bool_from_host_bool, [ast.Compare(left.args[0], [ast.IsNot()], [ast.Constant(True)])], [])
    elif is_always_host_numeric(right, 1, rte):
        return ast.Call(ppy_intrinsic_py_bool_from_host_bool, [left.args[0]], [])
    else:
        return None


def partial_eval_eq(left, right, rte):
    if isinstance(left, ast.Constant):
        if isinstance(right, ast.Constant):
            return ast.Constant(left.value == right.value)
        else:
            return partial_eval_eq(right, left, rte)
    # Checks for division, a bint cannot be 0
    elif is_always_python_numeric(right, 0, rte) and is_always_python_bint(left, rte) \
         or is_always_python_numeric(left, 0, rte) and is_always_python_bint(right, rte):
        return ast.Constant(False)
    elif is_always_host_numeric(right, 0, rte) and is_always_host_bint(left, rte) \
         or is_always_host_numeric(left, 0, rte) and is_always_host_bint(right, rte):
        return host_bool(False)
    # Special cases when either value is a bool
    elif isinstance(left, PPYValue) and left.type is ppy_bool_class:
        return partial_eval_eq_left_bool(left, right, rte)
    elif isinstance(right, PPYValue) and right.type is ppy_bool_class:
        return partial_eval_eq_left_bool(right, left, rte)
    elif is_always_host_int_from_bool(left, rte):
        return partial_eval_eq_left_host_int_from_bool(left, right, rte)
    elif is_always_host_int_from_bool(right, rte):
        return partial_eval_eq_left_host_int_from_bool(right, left, rte)

    return None


comparison_inverses = {
    ast.Is: ast.IsNot,
    ast.LtE: ast.Gt,
    ast.Lt: ast.GtE,
    ast.Eq: ast.NotEq
}

comparison_inverses.update({v: k for k, v in comparison_inverses.items()})


def reverse_comparison(comparison, rte):
    if len(comparison.ops) == 1:
        left = comparison.left
        right = comparison.comparators[0]

        op_type = type(comparison.ops[0])
        inverse_op = comparison_inverses[op_type]()

        if is_always_python_bool(left, rte) and isinstance(right, ast.Constant):
            if isinstance(inverse_op, ast.Is) and right.value is True:
                return left
            elif isinstance(inverse_op, ast.IsNot) and right.value is False:
                return left

        return ast.Compare(comparison.left, [inverse_op], comparison.comparators)
    else:
        raise NotImplementedError


def partial_eval_ne(left, right, rte):
    eq_res = partial_eval_eq(left, right, rte)
    if isinstance(eq_res, ast.Constant):
        if eq_res.value is True:
            return ast.Constant(False)
        elif eq_res.value is False:
            return ast.Constant(True)
    elif isinstance(eq_res, ast.UnaryOp) and isinstance(eq_res.op, ast.Not):
        return eq_res.operand
    elif isinstance(eq_res, ast.Call) and eq_res.func is ppy_intrinsic_py_bool_from_host_bool:
        arg0 = eq_res.args[0]

        if isinstance(arg0, ast.Compare):
            return ast.Call(ppy_intrinsic_py_bool_to_host_bool, [reverse_comparison(arg0, rte)], [])
    elif isinstance(eq_res, ast.Compare):
        return reverse_comparison(eq_res, rte)


    maybe_host_bool = get_host_bool(eq_res)

    if maybe_host_bool is None:
        return None
    else:
        return host_bool(not maybe_host_bool)


def partial_eval_is_not(left, right, rte):
    is_res = partial_eval_is(left, right, rte)

    if is_res:
        # an evaluation of is should always yield a bool
        if isinstance(is_res, ast.Constant):
            return ast.Constant(not is_res.value)
        else:
            return ast.UnaryOp(ast.Not, is_res)
    else:
        return None


def partial_eval_is(left, right, rte):
    if left in (ppy_intrinsic_absent, ppy_NotImplemented) \
            or right in (ppy_intrinsic_absent, ppy_NotImplemented):
        # TODO: this assumption can be removed once we have more solid type-checking
        # absent and NotImplemented are singletons which should always be resolvable statically
        # if a type is unknown, we assume it was not absent or NotImplemented
        # this assumption can hold here because absent and NotImplemented values being returned by a semantics
        # or a dunder is never specific to a value, but always to a whole type
        return ast.Constant(left is right)

    if isinstance(left, PPYClass) and isinstance(right, PPYClass):
        return ast.Constant(left is right)

    if isinstance(left, PPYValue) and isinstance(right, PPYValue):
        left_type = left.type
        right_type = right.type

        if left_type is not None and right_type is not None and left_type != right_type:
            return ast.Constant(False)
        if isinstance(left.origin, ast.Constant) and isinstance(right.origin, ast.Constant):
            return ast.Constant(left.value.value is right.value.value)

    if isinstance(left, PPYFunction) and isinstance(right, PPYFunction):
        return ast.Constant(left.origin is right.origin)

    # Unresolved
    return None


# ======================================================================================================================
#  Evaluation of module top-level
# ======================================================================================================================

def load_module(name, module, sys_modules):
    rte = RTE(sys_modules)
    this_module = PPYModule(origin=module, context=rte)
    sys_modules[name] = this_module
    rte._globals = this_module

    if name == "builtins":
        # Load some extra builtin objects
        populate_builtins(this_module)

    for stmt in module.body:
        if isinstance(stmt, ast.FunctionDef):
            partial_eval_def(stmt, rte)
        elif isinstance(stmt, ast.ClassDef):
            partial_eval_class(stmt, rte)
        elif isinstance(stmt, (ast.Import, ast.ImportFrom)):
            partial_eval_import(stmt, rte)
        else:
            raise NotImplementedError("PPY: modules can only contain import or class and function definitions")

    if name == "builtins":
        # Load some builtins in global scope
        bootstrap_builtins(this_module)
    elif name == "semantics":
        # Load semantics in __compiler_intrinsics__
        bootstrap_semantics(this_module)


def partial_eval_def(func_def, rte):
    decorators = func_def.decorator_list
    decorators_values = [partial_eval_expr(d, rte) for d in decorators]
    if ppy_intrinsic_define_semantics in decorators_values:
        ppy_func = PPYSemantics(origin=func_def, context=rte)
    elif rte.is_global():
        ppy_func = PPYFunction(origin=func_def, context=rte)
    else:
        ppy_func = PPYClosure(origin=func_def, context=rte)

    if any(not isinstance(d, PPYIntrinsic) for d in decorators_values):
        raise NotImplementedError("PPY: non-intrinsic decorators not supported")

    rte[func_def.name] = ppy_func


def partial_eval_class(class_def, rte):
    this_class = PPYClass(origin=class_def, context=rte)

    for stmt in class_def.body:
        if isinstance(stmt, ast.FunctionDef):
            this_class[stmt.name] = PPYFunction(origin=stmt, context=rte)
        elif isinstance(stmt, ast.Pass):
            pass
        else:
            raise NotImplementedError("PPY: classes can only contain method definitions")

    rte[class_def.name] = this_class


def partial_eval_import(import_stmt, rte):
    if isinstance(import_stmt, ast.ImportFrom):
        ppy_module = rte.modules[import_stmt.module]

        for alias in import_stmt.names:
            obj = ppy_module[alias.name]
            name = alias.asname or alias.name
            rte[name] = obj
    else:
        raise NotImplementedError("import [module]")


# ======================================================================================================================
#  Behavior computation wrappers
# ======================================================================================================================

def convert_expr_to_return_host_bool(expr):
    if isinstance(expr, ast.Call):
        func = expr.func
        if isinstance(func, ast.Name) and func.id == 'py_bool_from_host_bool':
            # assume correct number of argument
            return expr.args[0]
        else:
            raise TypeError(f"cannot convert call to a return-host-bool version due to unknown callee: {func}")
    elif isinstance(expr, ast.Compare):
        return ast.Call(ast.Name('py_bool_to_host_bool', ast.Load()), [expr], [])
    elif isinstance(expr, ast.Constant):
        val = expr.value
        if isinstance(val, bool):
            return ast.Call(ast.Name('py_bool_to_host_bool', ast.Load()), [expr], [])

    raise TypeError(f"cannot convert expr to a return-host-bool version: {expr}")


def convert_body_to_return_host_bool(body):
    if len(body) == 1:
        stmt = body[0]

        if isinstance(stmt, ast.Return):
            return [ast.Return(convert_expr_to_return_host_bool(stmt.value))]
        elif isinstance(stmt, ast.Raise):
            return body
        else:
            raise NotImplementedError(f"cannot convert body to a return-host-bool version, contains a {type(stmt)}")
    else:
        raise NotImplementedError("cannot convert body to a return-host-bool version due to len != 1")


def type_name_to_ppy(name, ppy_sys_modules):
    if name == "sint":
        return ppy_intrinsic_sint
    elif name == "bint":
        return ppy_intrinsic_bint
    elif name == "unknown":
        return None
    else:
        return ppy_sys_modules["builtins"][name]


def type_name_to_python(name):
    if name == "sint":
        return int
    elif name == "bint":
        return int
    elif name == "function":
        return types.FunctionType
    elif name == "method":
        return types.MethodType
    elif name == "range_iterator":
        return type(iter(range(42)))  # range_iterator
    elif name == "NotImplementedType":
        return type(NotImplemented)
    else:
        return eval(name)


def make_ast_simple_arguments(*args_names, annotations=()):
    return ast.arguments([], [ast.arg(n, t, None) for n, t in zip(args_names, annotations)], None, [], [], None, [])


def compute_single_behavior(behavior_name, module_name, callee_name, types, as_test, ppy_sys_modules):
    module = ppy_sys_modules[module_name]
    callee = module[callee_name]

    rte = RTE(ppy_sys_modules, globals=module)

    if isinstance(callee, PPYClass):
        fn = callee["__new__"]
        args = [callee,
                *(PPYValue.with_type_only(type_name_to_ppy(t, ppy_sys_modules)) for t in types)]
        args_names = [a.arg for a in fn.origin.args.args][1:]
    else:
        fn = callee
        args = [PPYValue.with_type_only(type_name_to_ppy(t, ppy_sys_modules)) for t in types]
        args_names = [a.arg for a in fn.origin.args.args]

    result_body = list(partial_eval_function_call(fn, args, [], rte, toplevel=True))

    annotations = [None if t == "unknown" else ast.Name(t, ast.Load()) for t in types]

    annotated_arguments = make_ast_simple_arguments(*args_names, annotations=annotations)

    behavior = ast.FunctionDef(behavior_name,
                               annotated_arguments,
                               result_body,
                               [ast.Name("define_behavior", ast.Load())],
                               None,
                               None)

    # We apply post-processing to behaviors beautify the code and remove statements which were made obsolete
    remove_extra_pass(behavior)
    AssignmentRemover(behavior).apply()
    DuplicateBranchingRemover(behavior).apply()
    DeadCodeRemover(behavior).apply()
    PPYValuesReplacer(behavior).apply()

    if as_test:
        behavior.body = convert_body_to_return_host_bool(behavior.body)

    return behavior


# Bootstrap base types
def dummy_class_def(name):
    return ast.parse(f"class {name}: pass")


ppy_type_class = PPYClass(context=None, origin=dummy_class_def("type").body[0], type="TMP", _mro=[])
ppy_object_class = PPYClass(context=None, origin=dummy_class_def("object").body[0], _mro=PPYClass.MRO_SELF)
ppy_module_class = PPYClass(context=None, origin=dummy_class_def("module").body[0], _mro=PPYClass.MRO_SELF_AND_OBJECT)
ppy_function_class = PPYClass(context=None, origin=dummy_class_def("function").body[0],
                              _mro=PPYClass.MRO_SELF_AND_OBJECT)
ppy_NotImplementedType = PPYClass(context=None, origin=dummy_class_def("NotImplementedType").body[0],
                                  _mro=PPYClass.MRO_SELF_AND_OBJECT)

ppy_type_class.type = ppy_type_class

ppy_NotImplemented = PPYSingleton(name="NotImplemented", type=ppy_NotImplementedType)
ppy_isinstance = PPYBuiltin(name="isinstance")
ppy_issubclass = PPYBuiltin(name="issubclass")
# NOTE: it is not exactly correct to treat type as a function, but we do not intend on handling metaclass anyway
ppy_type = PPYBuiltin(name="type")
ppy_int_class = None
ppy_bool_class = None
ppy_float_class = None
ppy_str_class = None


def populate_builtins(ppy_builtin):
    ppy_builtin["object"] = ppy_object_class
    ppy_builtin["NotImplemented"] = ppy_NotImplemented
    ppy_builtin["isinstance"] = ppy_isinstance
    ppy_builtin["issubclass"] = ppy_issubclass
    ppy_builtin["type"] = ppy_type


def bootstrap_builtins(ppy_builtin):
    global ppy_int_class, ppy_bool_class, ppy_float_class, ppy_str_class

    ppy_int_class = ppy_builtin["int"]
    ppy_bool_class = ppy_builtin["bool"]
    ppy_float_class = ppy_builtin["float"]
    ppy_str_class = ppy_builtin["str"]


def bootstrap_semantics(ppy_semantics):
    for name, item in ppy_semantics.items():
        if isinstance(item, PPYSemantics):
            intrinsic_name = f"semantics_{name}"
            ppy__compiler_intrinsics__[intrinsic_name] = item


def load_sempy_file(module_path, specializations, must_exist=True):
    path, ext = os.path.splitext(module_path)
    sempy_path = path + ".sempy"
    module_name = os.path.split(path)[-1]

    try:
        with open(sempy_path, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        if must_exist:
            raise FileNotFoundError(f"semPy requires a {module_name}.sempy file next to the module {module_path}")
        else:
            return

    exec(content, {"add_specializations": api.maker_specializations_adder(module_name, specializations)})


def compute_behaviors(semantics_file, builtins_file, more_modules):
    # Builtin modules must be preloaded, there is no dynamic loading
    ppy_sys_modules = PPYContainer(items={"__compiler_intrinsics__": ppy__compiler_intrinsics__})

    specializations = []

    # Preload builtins and semantics
    with open(semantics_file, 'r') as f:
        semantics_ast = ast.parse(f.read())

    load_sempy_file(semantics_file, specializations, must_exist=False)
    load_module("semantics", semantics_ast, ppy_sys_modules)

    with open(builtins_file, 'r') as f:
        builtins_ast = ast.parse(f.read())

    load_sempy_file(builtins_file, specializations, must_exist=False)
    load_module("builtins", builtins_ast, ppy_sys_modules)

    # Extra modules
    for filename in more_modules:
        module_path, _ = os.path.splitext(filename)
        module_name = os.path.split(module_path)[-1]

        with open(filename, 'r') as f:
            module_ast = ast.parse(f.read())

        load_sempy_file(filename, specializations, must_exist=False)
        load_module(module_name, module_ast, ppy_sys_modules)

    # Known intrinsics
    define_behavior = "define_behavior"
    other_intrinsics = "sint, bint, py_int_to_float, py_int_from_host, py_int_to_host, py_float_from_host, " \
                       "py_float_to_host, py_sint_to_host, py_bint_to_host, py_bool_from_host_bool, " \
                       "py_bool_to_host_bool, py_str_from_host, py_str_to_host, py_str_len_to_host, alloc"

    result = f"from __compiler_intrinsics__ import {define_behavior}, {other_intrinsics}\n\n"

    for specs in specializations:
        for behavior_name, types in specs:
            behavior = compute_single_behavior(behavior_name,
                                               specs.module,
                                               specs.function,
                                               types,
                                               specs.as_test,
                                               ppy_sys_modules)
            try:
                ast.fix_missing_locations(behavior)
                result += f"{ast.unparse(behavior)}\n\n"
            except Exception:
                logging.warning(f"ast.unparse failed to generate source for: {behavior.name}")
                raise

    return result
