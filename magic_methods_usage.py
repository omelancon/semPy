import argparse
import inspect
import pprint
import sys
from functools import wraps
from types import ModuleType

from utils import *


# ======================================================================================================================
#   Semantics Instructions
# ======================================================================================================================

class Behavior:
    pass


class Procedure(Behavior):
    def __init__(self, semantics, method, semantics_args, method_args):
        self.semantics = semantics
        self.method = method
        self.semantics_args = semantics_args
        self.method_args = method_args

    def __repr__(self):
        method_qualname = self.method.__qualname__
        return f"call to {method_qualname}"

    @property
    def is_reflected_magic_method(self):
        # TODO: slightly hacky, but does the job for now
        method_args = self.method_args
        semantics_args = self.semantics_args

        # reflected method call are detected by the reversal of arguments
        # we must use 'is' because == is True for 1 and 1.0
        # it is okay to use 'is' because arguments come from the 'instances' global list
        # this may not work under other implementations than cPython
        return all(x is y for x, y in zip(method_args, reversed(semantics_args))) \
               and not any(x is y for x, y in zip(method_args, semantics_args))

    @property
    def is_comparison(self):
        return self.semantics in ("eq", "ne", "ge", "gt", "le", "lt")


class Error(Behavior):
    def __init__(self, exc):
        self.exc_type = type(exc)
        self.exc_args = exc.args

    def __repr__(self):
        return f"raised {repr(self.exc_type(*self.exc_args))}"

    @property
    def error_message(self):
        return str(self.exc_type(*self.exc_args))


# ======================================================================================================================
#   __compiler_intrinsics__ mock module
# ======================================================================================================================

def get_current_semantics_context(semantics_register):
    for frame in inspect.stack():
        function_name = frame.function
        if function_name in semantics_register:
            function = frame.frame.f_globals[function_name]
            signature = inspect.signature(function).parameters
            args = tuple(frame.frame.f_locals[name] for name in signature.keys())
            return function_name, args
    return None, None


def make_compiler_intrinsics_module():
    target_semantics = [*templates.arithmetic_info,
                        *templates.inplace_arithmetic_info,
                        *templates.comparison_info,
                        *templates.equality_info,
                        *templates.unary_arithmetic_info]

    # Registers for this module
    semantics_register = {}
    decision_tree = {}

    def register_semantics(name, f):
        if name in target_semantics:
            semantics_register[name] = f
        return f

    # Module attributes
    absent = object()

    def define_semantics(f):
        # TODO: in some cases the semantics has a default behavior (ex: eq) undetected by the mock class_getattr
        # TODO: to fix requires extra inspection of the semantics body, it may be too much work for what it's worth

        if f.__name__ in target_semantics:
            return register_semantics(f.__name__, f)
        else:
            return f

    def get_own_attr(obj, name):
        return obj.__dict__.get(name, None)

    def class_getattr(instance, name):
        cls = type(instance)

        for super_cls in cls.mro():
            attr = get_own_attr(super_cls, name)

            if attr is not None:

                @wraps(attr)
                def wrapped_method(*args):
                    """
                    Wrapper that registers behaviour of the recovered method
                    """

                    # Gather positional information: in which semantics is this method being called?
                    current_semantics, semantics_args = get_current_semantics_context(semantics_register)

                    # For which types is it being called?
                    decision_tree_branch = decision_tree.setdefault(current_semantics, {})
                    for argument in semantics_args[:-1]:
                        decision_tree_branch = decision_tree_branch.setdefault(get_type_name(argument), {})

                    last_type_name = get_type_name(semantics_args[-1])

                    res = attr(*args)

                    if res is not NotImplemented:
                        decision_tree_branch[last_type_name] = Procedure(current_semantics, attr, semantics_args, args)

                    return res

                return wrapped_method

        return absent

    def py_bool_to_host_bool(arg):
        return arg

    # Create module
    _all = ["define_semantics", "class_getattr", "absent", "py_bool_to_host_bool"]
    _doc = "A mock version of __compiler_intrinsics__ which registers cPython method calls"

    module = ModuleType("__compiler_intrinsics__")

    module.__all__ = _all
    module.__doc__ = _doc

    for name in _all:
        setattr(module, name, locals()[name])

    return module, semantics_register, decision_tree


# ======================================================================================================================
#   decision tree
# ======================================================================================================================

def copy_type_behavior(decision_branch, source_type, target_type):
    if isinstance(decision_branch, dict):
        for type_name, behavior in decision_branch.items():
            copy_type_behavior(behavior, source_type, target_type)

        source_sub_branch = decision_branch[source_type]
        decision_branch[target_type] = source_sub_branch


def build_decision_tree(filename):
    compiler_intrinsics_module, semantics_register, decision_tree = make_compiler_intrinsics_module()

    with open(filename, 'r') as f:
        content = f.read()
        sys.modules["__compiler_intrinsics__"] = compiler_intrinsics_module

        exec(content, {})

    for name, semantics in semantics_register.items():
        signature = inspect.signature(semantics).parameters

        for left in instances:

            if len(signature) == 1:
                try:
                    semantics(left)
                except TypeError as e:
                    decision_tree.setdefault(name, {})[get_type_name(left)] = Error(e)
            elif len(signature) == 2:
                for right in instances:
                    try:
                        semantics(left, right)
                    except TypeError as e:
                        decision_tree.setdefault(name, {}).setdefault(get_type_name(left), {})[
                            get_type_name(right)] = Error(e)
            else:
                raise NotImplementedError(f"cannot handle semantics with {len(signature)} arguments")

    return pprint.pformat(decision_tree)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Generate zipi decision tree and behavior functions")
    parser.add_argument('semantics')
    parser.add_argument('-path', default=None)

    args = parser.parse_args()
    semantics_file = args.semantics
    path = args.path

    if path:
        with open(path, 'w') as f:
            f.write(build_decision_tree(semantics_file))
    else:
        print(build_decision_tree(semantics_file))
