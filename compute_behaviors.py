#!/usr/bin/env python3

import ast, argparse, copy, itertools, logging, operator, sys
from collections import Counter

from utils import *

try:
    ast.unparse
except AttributeError:
    logging.error("Behavior generation requires Python >=3.9")
    raise

# ======================================================================================================================
#   Parameters
# ======================================================================================================================

# Default value if not --int-maxsize argument is passed
INT_MAXSIZE = sys.maxsize

# ======================================================================================================================
#   AST traversal
# ======================================================================================================================

class AstRegister(ast.NodeVisitor):
    def __init__(self, ast_):
        self._register = {}
        self.visit(ast_)

    def __getitem__(self, item):
        return self._register[item]

    def __setitem__(self, item, value):
        self._register[item] = value

    def get(self, item, default=None):
        try:
            return self.__getitem__(item)
        except AttributeError:
            return default


class MethodRegister(AstRegister):
    def __init__(self, ast_, classes):
        super().__init__(ast_)
        self.classes = classes

    def __getitem__(self, item):
        for base_name in self._register['__mro__']:
            base = self.classes[base_name]
            method = base._register.get(item)

            if method is not None:
                return method

        raise AttributeError(item)

    def visit_FunctionDef(self, node):
        self[node.name] = node


class ClassRegister(AstRegister):
    def visit_ClassDef(self, node):
        self[node.name] = MethodRegister(node, self)
        self[node.name]['__mro__'] = (node.name,) + tuple(t.id for t in node.bases)

    def get_by_qualname(self, qualname):
        cls_name, method_name = qualname.split('.')
        method_register = self.get(cls_name)
        return method_register.get(method_name) if method_register else None


class SemanticsRegister(AstRegister):
    # Offers a register of semantics to be optimized to behaviors and a second register of all defined semantics
    # The second register must be accessed through the 'get_from_all_semantics' method
    def __init__(self, ast_):
        self._all_semantics = {}
        super().__init__(ast_)

    def visit_FunctionDef(self, node):
        decorators = node.decorator_list
        if any(isinstance(d, ast.Name) and d.id == 'define_semantics' for d in decorators):
            if node.name in target_semantics:
                self[node.name] = node
            self._all_semantics[node.name] = node

    def iter_binary_semantics(self):
        for name, sem in self._register.items():
            if len(sem.args.args) == 2:
                yield name, sem

    def iter_unary_semantics(self):
        for name, sem in self._register.items():
            if len(sem.args.args) == 1:
                yield name, sem

    def get_from_all_semantics(self, name, default=None):
        return self._all_semantics.get(name, default)


class AstNameInliner(ast.NodeTransformer):
    def __init__(self, table):
        self.table = table

    def visit_Name(self, node):
        return self.table.get((node.id, type(node.ctx).__name__), None) or node


intrinsics_inverses = {
    "py_int_from_host": "py_int_to_host",
    "py_float_from_host": "py_float_to_host",
    "py_bool_to_host_bool": "py_bool_from_host_bool"
}

intrinsics_inverses = {
    **intrinsics_inverses,
    **{v: k for k, v in intrinsics_inverses.items()}
}

py_to_host_number_table = {
    "int": "py_int_to_host",
    "sint": "py_sint_to_host",
    "bint": "py_bint_to_host",
    "float": "py_float_to_host",
}


def get_py_to_host_number_intrinsics(type_):
    return py_to_host_number_table.get(type_)


def intrinsics_are_inverse(left_func, right_func):
    try:
        return intrinsics_inverses[left_func] == right_func
    except KeyError:
        return False


class AstIntrinsicsCallSimplifier(ast.NodeTransformer):
    @classmethod
    def get_call_function_id(cls, call):
        func = call.func
        if isinstance(func, ast.Name):
            return func.id
        else:
            return None

    @classmethod
    def get_arg_call_function_id(cls, call, i):
        args = call.args
        if i < len(args) and isinstance(args[i], ast.Call):
            return cls.get_call_function_id(args[i])
        else:
            return None

    def visit_Call(self, node):
        node = self.generic_visit(node)

        func_name = self.get_call_function_id(node)
        first_arg_func_name = self.get_arg_call_function_id(node, 0)

        if intrinsics_are_inverse(func_name, first_arg_func_name):
            return node.args[0].args[0]

        return node


class AstConvertOpsToHost(ast.NodeTransformer):
    # TODO: convert BinOp, this was not required when this comment was written
    def __init__(self, ctx):
        self.ctx = ctx

    def visit_Compare(self, node):
        left = node.left
        comparators = node.comparators

        left_type = partial_eval_resolve_type(left, self.ctx)
        comparators_types = [partial_eval_resolve_type(c, self.ctx) for c in comparators]

        left_intrinsics = get_py_to_host_number_intrinsics(left_type)
        comparators_intrinsics = [get_py_to_host_number_intrinsics(t) for t in comparators_types]

        if left_intrinsics and all(comparators_intrinsics):
            host_comparison = ast.Compare(
                ast.Call(
                    ast.Name(left_intrinsics, ast.Load()), [left], []),
                node.ops,
                [ast.Call(ast.Name(i, ast.Load()), [c], []) for i, c in zip(comparators_intrinsics, comparators)])
            return ast.Call(
                ast.Name("py_bool_from_host_bool", ast.Load()),
                [host_comparison],
                [])
        return node


class AstNameCounter(ast.NodeVisitor, Counter):
    def visit_Name(self, node):
        self[node.id, type(node.ctx).__name__] += 1


def is_chained_calls(node, names):
    if names:
        if isinstance(node, ast.Call) and isinstance(func:=node.func, ast.Name) and func.id == names[0]:
            if len(node.args) == 1:
                return is_chained_calls(node.args[0], names[1:])
        return False
    else:
        return True


# ======================================================================================================================
#   Partial evaluation
# ======================================================================================================================

# Used by partial evaluator to preserve closure of a FunctionDef
class ClosureDef(ast.FunctionDef):
    def __init__(self, *args, closure=None):
        super().__init__(*args)
        self.closure = closure

    @classmethod
    def from_FunctionDef(cls, fd, ctx):
        cd = cls(*[getattr(fd, attr) for attr in ast.FunctionDef._fields], closure=ctx)
        return cd

    _fields = (
        'name',
        'args',
        'body',
        'decorator_list',
        'returns',
        'type_comment',
        'closure',
    )


class StaticValue(ast.Constant):
    _absent = object()

    def __init__(self, value):
        super().__init__(value)

    def __deepcopy__(self, memodict={}):
        # Ignore memodict as there should be no cycles in a tree
        # Do not copy the value as it might be comapred with is
        return StaticValue(self.value)

    @classmethod
    def absent(cls):
        return cls(cls._absent)

    @classmethod
    def NotImplemented(cls):
        return cls(NotImplemented)


class StmtSequence(ast.stmt):
    def __init__(self, body):
        self.body = body

    def __deepcopy__(self, memodict={}):
        # Ignore memodict as there should be no cycles in a tree
        return StmtSequence(copy.deepcopy(self.body, memodict))

    _fields = (
        'body',
    )


# ======================================================================================================================
#   Partial evaluation
# ======================================================================================================================

class Unknown:
    def __repr__(self):
        return "<unknown>"


_unknown = Unknown()


class VarContext:
    def __init__(self, type=_unknown, value=_unknown):
        self._type = type
        self.value = value

        if isinstance(value, StaticValue):
            if value.value is StaticValue._absent:
                self._type = 'absent'
            elif value.value is NotImplemented:
                self._type = 'NotImplementedType'
            elif value.value in {int, bool, float, str}:
                self._type = "type"

    @property
    def type(self):
        return get_type_alias(self._type)

    @property
    def specialized_type(self):
        return self._type

    def __repr__(self):
        return f"VarContext(type={self.type} ({self.specialized_type}), value={self.value})"


class Context:
    def __init__(self, semantics, classes, closure=None):
        self._locals = {}
        self._closure = closure if closure is not None else {}
        self._globals = {
            'absent': VarContext(value=StaticValue.absent()),
            'NotImplemented': VarContext(value=StaticValue.NotImplemented()),
            'int': VarContext(value=StaticValue(int)),
            'bool': VarContext(value=StaticValue(bool)),
            'float': VarContext(value=StaticValue(float)),
            'str': VarContext(value=StaticValue(str)),
            'function': VarContext(value=StaticValue(function)),
        }

        self.semantics = semantics
        self.classes = classes

    def __getitem__(self, item):
        loc = self._locals.get(item)
        clo = self._closure.get(item)
        glo = self._globals.get(item)

        val = loc or clo or glo
        if val:
            return val
        else:
            raise KeyError(item)

    def __setitem__(self, item, value):
        self._locals[item] = value

    def __contains__(self, item):
        try:
            self[item]
            return True
        except KeyError:
            return False

    def get(self, item, default=None):
        loc = self._locals.get(item)
        clo = self._closure.get(item)
        glo = self._globals.get(item)

        return loc or clo or glo or default

    def new(self):
        return Context(self.semantics, self.classes)

    def from_closure(self, closure):
        return Context(self.semantics, self.classes, closure=closure)

    def get_semantics(self, name, default=None):
        return self.semantics.get_from_all_semantics(name, default)


def optimize_body(body, ctx):
    for optimization in [inline_variables, convert_ops_to_host_version, resolve_intrinsics_inverses]:
        body = optimization(body, ctx)
    return body


def convert_ops_to_host_version(body, ctx):
    return [AstConvertOpsToHost(ctx).visit(stmt) for stmt in copy.deepcopy(body)]


def resolve_intrinsics_inverses(body, ctx):
    return [AstIntrinsicsCallSimplifier().visit(stmt) for stmt in copy.deepcopy(body)]


def inline_variables(body, ctx):
    """
    Replace Name(..., Load()) which appear exactly once in the body by its value in the context
    Since assignments are removed in the pre-evaluated code, this is necessary
    TODO: When a name is referenced but cannot be inlined, we should add an assignment at the beginning of the body
    """
    name_counter = AstNameCounter()
    for stmt in body:
        name_counter.visit(stmt)

    names = {name for name, _ in name_counter.keys()}

    inlining_table = {
        (name, "Load"): ctx.get(name).value
        for name in names
        if not name_counter[name, "Store"]
           and not name_counter[name, "Del"]
           and name_counter[name, "Load"] == 1
           and name in ctx
           and ctx.get(name).value is not _unknown
    }

    body_copy = copy.deepcopy(body)
    for stmt in body_copy:
        AstNameInliner(inlining_table).visit(stmt)

    return body_copy


def partial_eval(fn_ast, semantics, classes, *args):
    ast_args = fn_ast.args

    if ast_args.kwonlyargs or ast_args.kw_defaults or ast_args.defaults:
        raise NotImplementedError("partial_eval only supports no-default positional arguments")

    # For now we assume only positional args
    fn_args = ast_args.posonlyargs + ast_args.args

    if len(args) > len(fn_args):
        raise TypeError(f"partially evaluated function takes {len(fn_args)} context arguments, {len(args)} were given.")
    elif len(args) < len(fn_args):
        raise TypeError(
            f"partially evaluated function missing {len(fn_args) - len(args)} context arguments. Empty contexts must be given explicitly.")

    ctx = Context(semantics, classes)

    for ctx_var, arg in zip(args, fn_args):
        ctx[arg.arg] = ctx_var

    body = fn_ast.body
    return partial_eval_body(body, ctx)


def partial_eval_body(body, ctx):
    result = []

    for stmt in partial_eval_stmts(body, ctx):
        result.append(stmt)
        if isinstance(stmt, ast.Return) or isinstance(stmt, ast.Raise):
            break

    return optimize_body(result, ctx)


def partial_eval_stmts(stmts, ctx):
    for stmt in stmts:
        # filter out None which is a removed statement (assignment which was resolved)
        yield from filter(None, partial_eval_stmt(stmt, ctx))


def is_sint_value(val):
    return val in range(-INT_MAXSIZE - 1, INT_MAXSIZE + 1)


def is_bint_value(val):
    return val not in range(-INT_MAXSIZE - 1, INT_MAXSIZE + 1)


def partial_eval_resolve_type(expr, ctx):
    if isinstance(expr, ast.Constant):
        value = expr.value
        type_name = type(value).__name__

        if type_name == "int":
            if is_sint_value(value):
                return "sint"
            elif is_bint_value(value):
                return "bint"
            else:
                return "int"
        else:
            return type_name
    elif isinstance(expr, ast.Compare):
        # In the context of behavior which are only for builtin types, a comparison will always return a bool
        return 'bool'
    elif isinstance(expr, ast.UnaryOp):
        if isinstance(expr.op, ast.Not):
            return 'bool'
    elif isinstance(expr, ast.Name):
        var = ctx.get(expr.id)
        if var:
            return var.specialized_type
    elif isinstance(expr, ast.Call):
        return partial_eval_resolve_call_return_type(ctx, expr)

    return _unknown


def partial_eval_resolve_call_return_type(ctx, call):
    func = call.func

    # Resolve return types of intrinsics functions
    if isinstance(func, ast.Name):
        name = func.id
        if name == "py_int_from_host":
            return "int"
        elif name == "py_bool_from_host_bool":
            return "bool"
        elif name == "py_float_from_host":
            return "float"
        elif name == "py_str_from_host":
            return "str"

    return _unknown


def partial_eval_set(ctx, name, ast_val):
    if name in ctx:
        raise NotImplementedError(f"partial evaluation does not support re-assignation: {name}")
    elif isinstance(ast_val, ast.FunctionDef):
        ctx[name] = VarContext(type='function', value=ClosureDef.from_FunctionDef(ast_val, ctx))
    else:
        ctx[name] = VarContext(type=partial_eval_resolve_type(ast_val, ctx), value=ast_val)


def partial_eval_stmt(stmt, ctx):
    if isinstance(stmt, ast.If):
        test_result = partial_eval_expr(stmt.test, ctx)

        if isinstance(test_result, ast.Constant):
            if test_result.value:
                yield from partial_eval_stmts(stmt.body, ctx)
            else:
                yield from partial_eval_stmts(stmt.orelse, ctx)
        else:
            yield ast.If(test_result,
                         partial_eval_body(stmt.body, ctx),
                         partial_eval_body(stmt.orelse, ctx))
    elif isinstance(stmt, ast.Return):
        value = stmt.value
        if isinstance(value, ast.Call):
            yield from partial_eval_return_tail_call(value, ctx)
        elif isinstance(value, ast.Name):
            var = ctx.get(value.id)
            if var:
                if isinstance(var.value, StmtSequence):
                    yield from var.value.body
                elif var.value is not _unknown:
                    yield ast.Return(var.value)
                else:
                    yield ast.Return(ast.Name(value.id, ast.Load()))
            else:
                yield ast.Return(partial_eval_expr(value, ctx) if value is not None else value)
        else:
            yield ast.Return(partial_eval_expr(value, ctx) if value is not None else value)
    elif isinstance(stmt, ast.FunctionDef):
        partial_eval_set(ctx, stmt.name, stmt)
        yield None  # TODO: not ok in general, but should be in the case of behaviors where we inline local functions
    elif isinstance(stmt, ast.Assign):
        if len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            expr = partial_eval_expr(stmt.value, ctx)
            partial_eval_set(ctx, stmt.targets[0].id, expr)
            yield None  # TODO: not ok in general, but should be in the case of behaviors
        else:
            raise NotImplementedError("Unsupported assignment to multiple targets or non name targets")
    elif isinstance(stmt, ast.Raise):
        yield ast.Raise(partial_eval_expr(stmt.exc, ctx), None)
    else:
        yield stmt


def partial_eval_expr(expr, ctx):
    if isinstance(expr, ast.Call):
        return partial_eval_call(expr, ctx)
    elif isinstance(expr, ast.Compare):
        return partial_eval_compare(expr, ctx)
    elif isinstance(expr, ast.BoolOp):
        return partial_eval_bool_op(expr, ctx)
    elif isinstance(expr, ast.BinOp):
        return partial_eval_bin_op(expr, ctx)
    elif isinstance(expr, ast.UnaryOp):
        return partial_eval_un_op(expr, ctx)
    elif isinstance(expr, ast.Attribute):
        obj = partial_eval_expr(expr.value, ctx)

        if isinstance(obj, ast.Name):
            var = ctx.get(obj.id)
            if var and isinstance(var.value, StaticValue):
                try:
                    attr = getattr(var.value.value, expr.attr)
                    if isinstance(attr, (int, float, str)):
                        return ast.Constant(attr)
                except AttributeError:
                    pass
        return ast.Attribute(obj, expr.attr, expr.ctx)
    else:
        return expr


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
    operator = get_operator_from_ast(op)

    if isinstance(left, ast.Constant) and isinstance(right, ast.Constant) and operator:
        return ast.Constant(operator(left.value, right.value))

    return ast.BinOp(left, op, right)


def partial_eval_un_op(expr, ctx):
    operand = partial_eval_expr(expr.operand, ctx)
    return ast.UnaryOp(expr.op, operand)


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


def partial_eval_call(call, ctx):
    func = partial_eval_expr(call.func, ctx)
    args = [partial_eval_expr(arg, ctx) for arg in call.args]

    if isinstance(func, ast.Name):
        result = partial_eval_static_function_call(func.id, args, call.keywords, ctx)

        if isinstance(result, StmtSequence):
            body = result.body

            if len(body) == 1 and isinstance(body[0], ast.Return):
                return body[0].value
            else:
                return result
        else:
            return result
    else:
        return ast.Call(func, args, call.keywords)


def ast_always_returns(node):
    # TODO: does not cover all forms (missing: With, Try, AsyncFor, AsyncWith)
    if isinstance(node, list):
        return any(ast_always_returns(n) for n in node)
    elif isinstance(node, (ast.Return, ast.Raise)):
        return True
    elif isinstance(node, ast.For):
        return ast_always_returns(node.body) and ast_always_returns(node.orelse)
    elif isinstance(node, ast.If):
        return ast_always_returns(node.body) and ast_always_returns(node.orelse)
    elif isinstance(node, ast.While):
        return ast_always_returns(node.body) and ast_always_returns(node.orelse)
    else:
        return False


def partial_eval_return_tail_call(call, ctx):
    func = partial_eval_expr(call.func, ctx)
    args = [partial_eval_expr(arg, ctx) for arg in call.args]

    if isinstance(func, ast.Name):
        result = partial_eval_static_function_call(func.id, args, call.keywords, ctx)

        if isinstance(result, StmtSequence):
            yield from result.body
            if not ast_always_returns(result.body):
                yield ast.Return(None)
        else:
            yield ast.Return(result)
    else:
        yield ast.Return(ast.Call(func, args, call.keywords))


def partial_eval_compare(cmp, ctx):
    left = partial_eval_expr(cmp.left, ctx)

    if len(cmp.comparators) > 1:
        raise NotImplementedError("partial_eval_compare: chain comparison not supported")
    else:
        op = cmp.ops[0]
        right = partial_eval_expr(cmp.comparators[0], ctx)

        if isinstance(op, ast.Is):
            res = partial_eval_is(left, right, ctx)
        elif isinstance(op, ast.IsNot):
            res = partial_eval_is_not(left, right, ctx)
        elif isinstance(op, ast.Eq):
            res = partial_eval_eq(left, right, ctx)
        elif isinstance(op, ast.NotEq):
            res = partial_eval_ne(left, right, ctx)
        elif isinstance(op, ast.Lt):
            res = partial_eval_lt(left, right, ctx)
        elif isinstance(op, ast.LtE):
            res = partial_eval_le(left, right, ctx)
        elif isinstance(op, ast.Gt):
            res = partial_eval_gt(left, right, ctx)
        elif isinstance(op, ast.GtE):
            res = partial_eval_ge(left, right, ctx)
        else:
            res = None

        if res is None:
            return ast.Compare(left, [op], [right])
        else:
            return res


def resolve_expression_sign(expr, ctx):
    if isinstance(expr, ast.Name):
        var = ctx.get(expr.id)

        if is_chained_calls(var.value, ["py_int_from_host", "py_str_len_to_host"]):
            return 1, False
    return None, None


# We implemented limited mechanism to detect whether a value is positive or negative
# This is mainly aimed at resolving the sign of int values coming from length of a sequence
def partial_eval_lt(left, right, ctx):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, ctx)

        if sign is not None:
            if sign == -1:
                if strict:
                    return ast.Constant(True)
            else:  # 0 or 1
                return ast.Constant(False)

    return None


def partial_eval_le(left, right, ctx):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, ctx)

        if sign is not None:
            if sign == -1 or sign == 0:
                return ast.Constant(True)

            elif strict: # > 0
                return ast.Constant(False)

    return None


def partial_eval_gt(left, right, ctx):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, ctx)

        if sign is not None:
            if sign == 1:
                if strict:
                    return ast.Constant(True)
            else:  # 0 or -1
                return ast.Constant(False)

    return None


def partial_eval_ge(left, right, ctx):
    if isinstance(right, ast.Constant) and right.value == 0:
        sign, strict = resolve_expression_sign(left, ctx)

        if sign is not None:
            if sign == 1 or sign == 0:
                return ast.Constant(True)

            elif strict: # > 0
                return ast.Constant(False)

    return None


def partial_eval_is_not(left, right, ctx):
    is_res = partial_eval_is(left, right, ctx)

    if is_res:
        # an evaluation of is should always yield a bool constant
        if isinstance(is_res, ast.Constant):
            return ast.Constant(not is_res.value)
        else:
            return ast.UnaryOp(ast.Not, is_res)
    else:
        return None


def partial_eval_is(left, right, ctx):
    if isinstance(left, ast.Name) and isinstance(right, ast.Name):
        left_var = ctx.get(left.id)
        right_var = ctx.get(right.id)

        if left_var and right_var:
            left_type = left_var.type
            right_type = right_var.type
            if left_type in ("absent", "NotImplementedType") or right_type in ("absent", "NotImplementedType"):
                # TODO: this assumption can be removed once we have more solid type-checking
                # 'absent' and 'NotImplemented' are singletons which should always be resolvable statically
                # if a type is unknown, we assume it was not absent or NotImplemented
                # this assumption can hold here because absent and NotImplemented values being returned by a semantics
                # or a dunder is never specific to a value, but always to a whole type
                return ast.Constant(left_type == right_type)
            if left_var.type != _unknown != right_var.type and left_var.type != right_var.type:
                return ast.Constant(False)
            if isinstance(left_var.value, ast.Constant) and isinstance(right_var.value, ast.Constant):
                return ast.Constant(left_var.value.value is right_var.value.value)
    # Unresolved
    return None


def partial_eval_eq(left, right, ctx):
    if isinstance(left, ast.Constant):
        if isinstance(right, ast.Constant):
            return ast.Constant(left.value == right.value)
        else:
            return partial_eval_eq(right, left, ctx)
    elif isinstance(right, ast.Constant):
        if right.value == 0 and isinstance(left, ast.Name):
            left_type = ctx.get(left.id).specialized_type
            if left_type == 'bint':
                return ast.Constant(False)
            elif left_type == 'bool':
                return ast.UnaryOp(ast.Not(), left)
    return None


def partial_eval_ne(left, right, ctx):
    eq_res = partial_eval_eq(left, right, ctx)
    if isinstance(eq_res, ast.Constant):
        if eq_res.value is True:
            return ast.Constant(False)
        elif eq_res.value is False:
            return ast.Constant(True)
    elif isinstance(eq_res, ast.UnaryOp) and isinstance(eq_res.op, ast.Not):
        return eq_res.operand
    return None


def partial_eval_static_function_call(func_name, args, keywords, ctx):
    # Assume here that builtins are called with the correct number of arguments
    if func_name == "isinstance":
        instance = args[0]
        type_info = args[1]

        if isinstance(instance, ast.Name) and isinstance(type_info, ast.Name):
            instance_name = instance.id
            type_info_name = type_info.id

            instance_ctx = ctx.get(instance_name)

            if instance_ctx:
                instance_actual_type = instance_ctx.type

                if instance_actual_type is _unknown:
                    raise TypeError(f"partial_eval_static_function_call: type of '{instance_name}' is unknown")
                elif type_info_name == "sint":
                    # TODO: incorrect but temporarily works for index semantics
                    return ast.Constant(True)
                elif type_info_name == "bint":
                    # TODO: incorrect but temporarily works for index semantics
                    return ast.Constant(False)
                elif issubclass(eval(instance_actual_type), eval(type_info_name)):
                    return ast.Constant(True)
                elif instance_actual_type in types:
                    return ast.Constant(False)
            else:
                raise NameError(f"partial_eval_static_function_call: could not resolve name '{instance_name}'")

    elif func_name == "type":
        instance = args[0]

        if isinstance(instance, ast.Name):
            instance_name = instance.id

            instance_ctx = ctx.get(instance_name)

            if instance_ctx:
                instance_actual_type = instance_ctx.type

                if instance_actual_type is not _unknown:
                    return ast.Name(instance_actual_type, ast.Load())
                else:
                    raise TypeError(f"partial_eval_static_function_call: type of '{instance_name}' is unknown")

            else:
                raise NameError(f"partial_eval_static_function_call: could not resolve name '{instance_name}'")
        else:
            raise NotImplementedError(f"partial_eval_static_function_call: could not type of '{instance}'")

    elif func_name in ctx:
        return partial_eval_local_function_call(ctx[func_name], args, ctx)
    else:
        return partial_eval_specialize_intrinsic_function(func_name, args, keywords, ctx)


def partial_eval_resolved_function_call(fn_ast, args, ctx):
    fn_args = fn_ast.args.args
    name_table = {}

    if len(args) == len(fn_args):
        call_ctx = ctx.from_closure(fn_ast.closure) if isinstance(fn_ast, ClosureDef) else ctx.new()

        for fn_arg, arg in zip(fn_args, args):
            if isinstance(arg, ast.Name):
                arg_name = fn_arg.arg
                arg_value = ctx[arg.id]
                for ast_ctx in ["Load", "Store", "Del"]:
                    name_table[(arg_name, ast_ctx)] = ast.Name(arg.id, ast_ctx)
                call_ctx[arg_name] = arg_value
            else:
                raise NotImplementedError("partial_eval_local_function_call: non-name argument")

        body = fn_ast.body

        result_body = StmtSequence(partial_eval_body(body, call_ctx))

        # Important to use a deepcopy of the ast so renaming does not affect called method variables
        body_copy = copy.deepcopy(result_body)
        AstNameInliner(name_table).visit(body_copy)
        return body_copy

    else:
        raise TypeError("partial_eval_local_function_call: incorrect number of arguments")


def partial_eval_local_function_call(func, args, ctx):
    fn_ast = func.value

    if isinstance(fn_ast, ast.FunctionDef):
        return partial_eval_resolved_function_call(fn_ast, args, ctx)
    else:
        raise ValueError("partial evaluation call to non-function local object")


def partial_eval_specialize_intrinsic_function(func_name, args, keywords, ctx):
    # Assume here that builtins are called with the correct number of arguments
    if func_name == "py_int_to_host":
        self = args[0]
        if isinstance(self, ast.Name):
            name = self.id

            name_ctx = ctx.get(name)

            if name_ctx is not None:
                type_ = name_ctx.specialized_type

                if type_ == "sint":
                    return ast.Call(ast.Name("py_sint_to_host", ast.Load()), args, [])
                elif type_ == "bint":
                    return ast.Call(ast.Name("py_bint_to_host", ast.Load()), args, [])
                elif type_ == "bool":
                    return ast.Call(ast.Name("py_bool_to_host_int", ast.Load()), args, [])
                elif issubclass(eval(type_), int):
                    return ast.Call(ast.Name("py_int_to_host", ast.Load()), args, [])
    elif func_name == "class_getattr":
        return partial_eval_class_getattr_call(args, ctx)
    elif func_name == "alloc":
        return partial_eval_alloc_call(args, keywords, ctx)

    semantics = ctx.get_semantics(func_name)
    if semantics:
        return partial_eval_resolved_function_call(semantics, args, ctx)

    # No specialization
    return ast.Call(ast.Name(func_name, ast.Load()), args, [])


def partial_eval_class_getattr_call(args, ctx):
    # Assume correct arity
    name = args[0]
    attr = args[1]

    if isinstance(name, ast.Name):
        if isinstance(attr, ast.Constant) and isinstance(attr.value, str):
            obj = ctx.get(name.id)

            if obj is None:
                raise NameError(f"partial_eval: could not resolve {name.id}")
            elif obj.type is _unknown:
                raise NotImplementedError(f"partial_eval_class_getattr_call: could not resolve type of '{name.id}'")
            else:
                obj_type = obj.type
                attr_name = attr.value

                cls = ctx.classes[obj_type]
                attr = cls.get(attr_name, StaticValue.absent())

                return attr

        else:
            raise ValueError("partial_eval_class_getattr_call: second argument must be a string literal")
    else:
        raise NotImplementedError("partial_eval_class_getattr_call: first argument must have been resolved to a name")


def partial_eval_alloc_call(args, keywords, ctx):
    # TODO: partial eval of keywords
    return ast.Call(ast.Name("alloc", ast.Load()), args, keywords)


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


def get_behavior_name(semantics, types):
    type_signature = '-'.join(t + id_ for t, id_ in zip(types, 'XYZWABCDEF'))
    return f"py-{semantics}-{type_signature}"


def make_ast_raise_with_msg(error_name, msg):
    exc = ast.Call(ast.Name(error_name, ast.Load()), [ast.Constant(msg)], [])
    return ast.Raise(exc, None)


def make_ast_simple_arguments(*args_names, annotations=()):
    return ast.arguments([], [ast.arg(n, t, None) for n, t in itertools.zip_longest(args_names, annotations)], None, [],
                         [], None, [])


def get_subtree_nested_item(tree, chain):
    for x in chain:
        tree = tree[x]
    return tree


def build_semantics(semantics_file, builtins_file):
    with open(builtins_file, 'r') as f:
        builtins_ast = ast.parse(f.read())

    with open(semantics_file, 'r') as f:
        semantics_ast = ast.parse(f.read())

    class_register = ClassRegister(builtins_ast)
    semantics_register = SemanticsRegister(semantics_ast)

    behaviors = []

    define_behavior = "define_behavior"
    other_intrinsics = "py_int_from_host, py_int_to_host, py_bool_to_host_int, py_float_from_host, " \
                       "py_float_to_host, py_sint_to_host, py_bint_to_host, py_bool_from_host_bool, " \
                       "py_bool_to_host_bool, py_str_from_host, py_str_to_host, py_str_len_to_host, alloc"

    behavior_decorator_list = [ast.Name(f"{define_behavior}", ast.Load())]

    def register_behavior(name, sem, *types):
        args_names = [a.arg for a in sem.args.args]
        annotations = [None if t is _unknown else ast.Name(t, ast.Load()) for t in types]

        annotated_arguments = make_ast_simple_arguments(*args_names, annotations=annotations)
        behavior_name = get_behavior_name(name, [t for t in types if t is not _unknown])
        behavior_func_name = behavior_name.replace('-', '_')

        result_body = partial_eval(sem, semantics_register, class_register,
                                   *[VarContext(type=t) for t in types])

        behavior_func = ast.FunctionDef(behavior_func_name, annotated_arguments, result_body,
                                        behavior_decorator_list, None, None)

        behaviors.append(behavior_func)

        # For comparisons, we generate a version of the behavior which returns a host bool
        if name in ("eq", "ne", "ge", "gt", "le", "lt"):
            test_behavior_func_name = behavior_name.replace('py-', 'py-test-').replace('-', '_')

            test_body = convert_body_to_return_host_bool(result_body)
            test_behavior_func = ast.FunctionDef(test_behavior_func_name, annotated_arguments, test_body,
                                                 behavior_decorator_list, None, None)
            behaviors.append(test_behavior_func)

    for name, bin_semantics in semantics_register.iter_binary_semantics():
        for left_type in types_without_int:
            for right_type in types_without_int:
                if (name, left_type, right_type) not in binary_skip:
                    register_behavior(name, bin_semantics, left_type, right_type)

    for name, un_semantics in semantics_register.iter_unary_semantics():
        for type_ in types_without_int:
            register_behavior(name, un_semantics, type_)

    # special case
    for type_ in types_without_int:
        register_behavior("descriptor_get", semantics_register["descriptor_get"], type_, _unknown, _unknown)

    result = ""

    result += f"from __compiler_intrinsics__ import {define_behavior}, {other_intrinsics}\n\n"

    for b in behaviors:
        try:
            ast.fix_missing_locations(b)
            result += f"{ast.unparse(b)}\n\n"
        except Exception:
            logging.warning(f"ast.unparse failed to generate source for: {b.name}")
            raise

    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate zipi decision tree and behavior functions")
    parser.add_argument('semantics')
    parser.add_argument('builtins')
    parser.add_argument('-path', default=None)
    parser.add_argument('--int-maxsize', dest='int_maxsize', type=int, default=-1)

    args = parser.parse_args()
    semantics_file = args.semantics
    builtins_file = args.builtins
    path = args.path
    int_maxsize = args.int_maxsize

    if int_maxsize != -1:
        INT_MAXSIZE = int_maxsize

    if path:
        with open(path, 'w') as f:
            f.write(build_semantics(semantics_file, builtins_file))
    else:
        print(build_semantics(semantics_file, builtins_file))
