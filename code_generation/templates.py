# This file contains template for generating semantics and builtin classes

# ======================================================================================================================
#   semantics templates
# ======================================================================================================================

semantics_template = \
    """from __compiler_intrinsics__ import define_semantics, class_getattr, py_bool_to_host_bool, absent

{arithmetic}

@define_semantics
def maybe_trunc(obj):
    __trunc__ = class_getattr(obj, "__trunc__")
    if __trunc__ is absent:
        return absent
    else:
        result = __trunc__(obj)

        if type(result) is int:
            return result
        else:
            raise TypeError("__trunc__ returned non-int type: '" + type(obj).__name__ + "'")

@define_semantics
def trunc(obj):
    result = maybe_trunc(obj)
    if result is absent:
        raise TypeError("type '" + type(obj).__name__ + "' doesn't define __trunc__ method")
    else:
        return result

@define_semantics
def maybe_to_int(obj):
    __int__ = class_getattr(obj, "__int__")
    if __int__ is absent:
        return absent
    else:
        result = __int__(obj)

        if type(result) is int:
            return result
        else:
            raise TypeError("__int__ returned non-int type: '" + type(obj).__name__ + "'")

@define_semantics
def to_int(obj):
    result = maybe_to_int(obj)
    if result is absent:
        raise TypeError("'" + type(obj).__name__ + "' object cannot be interpreted as an integer")
    else:
        return result

@define_semantics
def maybe_to_float(obj):
    __float__ = class_getattr(obj, "__float__")
    if __float__ is absent:
        return absent
    else:
        result = __float__(obj)

        if isinstance(result, float):
            return result
        else:
            raise TypeError("__float__ returned non-float type: '" + type(obj).__name__ + "'")

@define_semantics
def to_float(obj):
    result = maybe_to_float(obj)
    if result is absent:
        raise TypeError("'" + type(obj).__name__ + "' object cannot be interpreted as a float")
    else:
        return result

@define_semantics
def maybe_index(obj):
    __index__ = class_getattr(obj, "__index__")
    if __index__ is absent:
        return absent
    else:
        result = __index__(obj)

        if result is absent:
            return absent
        elif isinstance(result, sint):
            return result
        elif isinstance(result, bint):
            raise OverflowError("cannot fit 'int' into an index-sized integer")
        else:
            raise TypeError("__index__ returned non-int type: '" + type(obj).__name__ + "'")

@define_semantics
def index(obj):
    result = maybe_index(obj)
    if result is absent:
        raise TypeError("'" + type(obj).__name__ + "' object cannot be interpreted as an integer")
    else:
        return result

@define_semantics
def maybe_big_index(obj):
    __index__ = class_getattr(obj, "__index__")
    if __index__ is absent:
        return absent
    else:
        result = __index__(obj)

        if result is absent:
            return absent
        elif type(result) is int:
            return result
        else:
            raise TypeError("__index__ returned non-int type: '" + type(obj).__name__ + "'")

@define_semantics
def big_index(obj):
    result = maybe_big_index(obj)
    if result is absent:
        raise TypeError("'" + type(obj).__name__ + "' object cannot be interpreted as an integer")
    else:
        return result

@define_semantics
def maybe_length(obj):
    __len__ = class_getattr(obj, "__len__")
    if __len__ is absent:
        return absent
    else:
        len_result = __len__(obj)
        index_result = index(len_result)
        if index_result < 0:
            raise ValueError("__len__() should return >= 0")
        else:
            return index_result

@define_semantics
def length(obj):
    result = maybe_length(obj)
    if result is absent:
        raise TypeError("object of type" + type(obj).__name__ + "has no len()")
    else:
        return result

@define_semantics
def truth(obj):
    __bool__ = class_getattr(obj, "__bool__")
    if __bool__ is not absent:
        result = __bool__(obj)
        if type(result) is bool:
            return result
        else:
            raise TypeError("__bool__ should return bool, returned '" + type(obj).__name__ + "'")
    else:
        len_result = maybe_length(obj)
        if len_result is not absent:
            return len_result != 0
        else:
            return True

@define_semantics
def test(obj):
    return py_bool_to_host_bool(truth(obj))

@define_semantics
def getattribute(obj, attr):
    __getattribute__ = class_getattr(obj, "__getattribute__")
    try:
        return __getattribute__(obj, attr)
    except AttributeError as e:
        __getattr__ = class_getattr(obj, "__getattr__")
        if __getattr__ is absent:
            raise e
        else:
            return __getattr__(obj, attr)

@define_semantics
def setattribute(obj, attr, val):
    __setattr__ = class_getattr(obj, "__setattr__")
    return __setattr__(obj, attr, val)

@define_semantics
def getitem(obj, index):
    __getitem__ = class_getattr(obj, "__getitem__")
    if __getitem__ is absent:
        raise TypeError("object is not subscriptable")
    else:
        return __getitem__(obj, index)

@define_semantics
def setitem(obj, index, value):
    __setitem__ = class_getattr(obj, "__setitem__")
    if __setitem__ is absent:
        raise TypeError("object does not support item assignment")
    else:
        return __setitem__(obj, index, value)

@define_semantics
def delitem(obj, index):
    __delitem__ = class_getattr(obj, "__delitem__")
    if __delitem__ is absent:
        raise TypeError("object does not support item deletion")
    else:
        return __delitem__(obj, index)

@define_semantics
def enter(obj):
    __enter__ = class_getattr(obj, "__enter__")
    if __enter__ is absent:
        raise AttributeError("__enter__")
    else:
        return __enter__(obj)

@define_semantics
def exit(obj, exc):
    __exit__ = class_getattr(obj, "__exit__")
    if __exit__ is absent:
        raise AttributeError("__exit__")
    elif exc is None:
        return __exit__(obj, None, None, None)
    else:
        # TODO: pass traceback as 4th arg to __exit__ once it exists
        exit_result = __exit__(obj, type(exc), exc, None)
        if exit_result:
            return
        else:
            raise exc

@define_semantics
def descriptor_get(attr, instance, owner):
    __get__ = class_getattr(attr, "__get__")
    if __get__ is absent:
        return attr
    else:
        return __get__(attr, instance, owner)"""

arithmetic_template = \
    """# Auto-generated
@define_semantics
def {op}(x, y):
    def normal():
        magic_method = class_getattr(x, "__{magic_method}__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__r{magic_method}__")
        if magic_method is absent:
            return err()
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return err()
            else:
                return result

    def err():
        raise TypeError("unsupported operand type(s) for {symbol}: '" + type(x).__name__ + "' and '" + type(y).__name__ + "'")

    return normal()"""

arithmetic_info = {'add': {"op": "add", "magic_method": "add", "symbol": "+"},
                   'bitand': {"op": "bitand", "magic_method": "and", "symbol": "&"},
                   'bitor': {"op": "bitor", "magic_method": "or", "symbol": "|"},
                   'floordiv': {"op": "floordiv", "magic_method": "floordiv", "symbol": "//"},
                   'lshift': {"op": "lshift", "magic_method": "lshift", "symbol": "<<"},
                   'matmul': {"op": "matmul", "magic_method": "matmul", "symbol": "@"},
                   'mod': {"op": "mod", "magic_method": "mod", "symbol": "%"},
                   'mul': {"op": "mul", "magic_method": "mul", "symbol": "*"},
                   'pow': {"op": "pow", "magic_method": "pow", "symbol": "**"},
                   'rshift': {"op": "rshift", "magic_method": "rshift", "symbol": ">>"},
                   'sub': {"op": "sub", "magic_method": "sub", "symbol": "-"},
                   'truediv': {"op": "truediv", "magic_method": "truediv", "symbol": "/"},
                   'xor': {"op": "xor", "magic_method": "xor", "symbol": "^"},
                   }

inplace_arithmetic_template = \
    """# Auto-generated
@define_semantics
def i{op}(x, y):
    def inplace():
        magic_method = class_getattr(x, "__i{magic_method}__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__{magic_method}__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__r{magic_method}__")
        if magic_method is absent:
            return err()
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return err()
            else:
                return result

    def err():
        raise TypeError("unsupported operand type(s) for {symbol}: '" + type(x).__name__ + "' and '" + type(y).__name__ + "'")

    return inplace()"""

inplace_arithmetic_info = {'iadd': {"op": "add", "magic_method": "add", "symbol": "+="},
                           'ibitand': {"op": "bitand", "magic_method": "and", "symbol": "&="},
                           'ibitor': {"op": "bitor", "magic_method": "or", "symbol": "|="},
                           'ifloordiv': {"op": "floordiv", "magic_method": "floordiv", "symbol": "//="},
                           'ilshift': {"op": "lshift", "magic_method": "lshift", "symbol": "<<="},
                           'imatmul': {"op": "matmul", "magic_method": "matmul", "symbol": "@="},
                           'imod': {"op": "mod", "magic_method": "mod", "symbol": "%="},
                           'imul': {"op": "mul", "magic_method": "mul", "symbol": "*="},
                           'ipow': {"op": "pow", "magic_method": "pow", "symbol": "**="},
                           'irshift': {"op": "rshift", "magic_method": "rshift", "symbol": ">>="},
                           'isub': {"op": "sub", "magic_method": "sub", "symbol": "-="},
                           'itruediv': {"op": "truediv", "magic_method": "truediv", "symbol": "/="},
                           'ixor': {"op": "xor", "magic_method": "xor", "symbol": "^="},
                           }

unary_arithmetic_template = \
"""# Auto-generated
@define_semantics
def {op}(x):
    def normal():
        magic_method = class_getattr(x, "__{magic_method}__")
        if magic_method is absent:
            return err()
        else:
            return magic_method(x)

    def err():
        raise TypeError("bad operand type for unary {symbol}: '" + type(x).__name__ + "'")

    return normal()"""

unary_arithmetic_info = {
    "pos": {"op": "pos", "magic_method": "pos", "symbol": "+"},
    "neg": {"op": "neg", "magic_method": "neg", "symbol": "-"},
    "invert": {"op": "invert", "magic_method": "invert", "symbol": "~"},
}

comparison_template = \
    """# Auto-generated
@define_semantics
def {op}(x, y):
    def normal():
        magic_method = class_getattr(x, "__{magic_method}__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__{reflected_magic_method}__")
        if magic_method is absent:
            return err()
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return err()
            else:
                return result

    def err():
        raise TypeError("'{symbol}' not supported between instances of '" + type(x).__name__ + "' and '" + type(y).__name__ + "'")

    return normal()"""

comparison_info = {
    "ge": {"op": "ge", "magic_method": "ge", "reflected_magic_method": "le", "symbol": ">="},
    "gt": {"op": "gt", "magic_method": "gt", "reflected_magic_method": "lt", "symbol": ">"},
    "le": {"op": "le", "magic_method": "le", "reflected_magic_method": "ge", "symbol": "<="},
    "lt": {"op": "lt", "magic_method": "lt", "reflected_magic_method": "gt", "symbol": "<"}
}

equality_template = \
    """# Auto-generated
@define_semantics
def {op}(x, y):
    def normal():
        magic_method = class_getattr(x, "__{magic_method}__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__{reflected_magic_method}__")
        if magic_method is absent:
            return default()
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return default()
            else:
                return result

    def default():
        return x {default_symbol} y

    return normal()"""

equality_info = {
    "eq": {"op": "eq", "magic_method": "eq", "reflected_magic_method": "eq", "default_symbol": "is"},
    "ne": {"op": "ne", "magic_method": "ne", "reflected_magic_method": "ne", "default_symbol": "is not"},
}

# ======================================================================================================================
#   int class templates
# ======================================================================================================================


int_binary_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) {op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_reflected_binary_method_template = \
    """
    def __r{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) {op} py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__r{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_inplace_binary_method_template = \
    """
    def __i{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) {op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__i{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_shift_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_reflected_shift_method_template = \
    """
    def __r{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__r{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_inplace_shift_method_template = \
    """
    def __i{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__i{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_division_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return {box_method}(py_int_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ZeroDivisionError("{error_message}")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_reflected_division_method_template = \
    """
    def __r{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) != py_int_to_host(0):
                    return {box_method}(py_int_to_host(other) {op} py_int_to_host(self))
                else:
                    raise ZeroDivisionError("{error_message}")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__r{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_inplace_division_method_template = \
    """
    def __i{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return {box_method}(py_int_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ZeroDivisionError("{error_message}")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__i{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_comparison_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) {op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

int_unary_method_template = \
    """
    def __{method_name}__(self):
        if isinstance(self, int):
            return {expr}
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'int' object but received a '" + type(self).__name__ + "'")
"""

class_int_template = \
    """
@builtin
@private
def convert_to_int(obj):
    int_conversion = semantics_maybe_to_int(obj)
    if int_conversion is absent:
        index_conversion = semantics_maybe_index(obj)
        if index_conversion is absent:
            trunc_conversion = semantics_maybe_trunc(obj)
            if trunc_conversion is absent:
                raise TypeError("int() argument must be a string, a bytes-like object or a number, not '" + type(obj).__name__ + "'")
            else:
                return trunc_conversion
        else:
            return index_conversion
    else:
        return int_conversion

@builtin
class int:
    def __new__(cls, val=absent):
        if cls is int:
            if val is absent:
                return 0
            else:
                return convert_to_int(val)
        elif isinstance(cls, type) and issubclass(cls, int):
            if val is absent:
                return alloc(int, cls=cls, value=py_int_to_host(0))
            else:
                return alloc(int, cls=cls, value=py_int_to_host(convert_to_int(val)))
        else:
            raise TypeError("int.__new__ expected a subtype of 'int' as first argument")

    def __bool__(self):
        if isinstance(self, int):
            return self != 0
        else:
            raise TypeError("descriptor '__bool__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __index__(self):
        if isinstance(self, int):
            return py_int_from_host(py_int_to_host(self))
        else:
            raise TypeError("descriptor '__index__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __abs__(self):
        if isinstance(self, int):
            if self < 0:
                return py_int_from_host(-py_int_to_host(self))
            else:
                return py_int_from_host(py_int_to_host(self))
        else:
            raise TypeError("descriptor '__abs__' requires a 'int' object but received a '" + type(self).__name__ + "'")
{methods}"""

int_method_info = {
    'add': {"method_name": "add", "op": "+"},
    'bitand': {"method_name": "and", "op": "&"},
    'bitor': {"method_name": "or", "op": "|"},
    'mul': {"method_name": "mul", "op": "*"},
    'pow': {"method_name": "pow", "op": "**"},
    'sub': {"method_name": "sub", "op": "-"},
    'xor': {"method_name": "xor", "op": "^"}
}

int_shift_method_info = {
    'lshift': {"method_name": "lshift", "op": "<<"},
    'rshift': {"method_name": "rshift", "op": ">>"},
}

int_division_method_info = {
    'floordiv': {"method_name": "floordiv", "box_method": "py_int_from_host", "op": "//",
                 "error_message": "integer division by zero"},
    'truediv': {"method_name": "truediv", "box_method": "py_float_from_host", "op": "/", "error_message": "division by zero"},
    'mod': {"method_name": "mod", "box_method": "py_int_from_host", "op": "%", "error_message": "modulo by zero"}
}

int_comparison_method_info = {
    'eq': {"method_name": "eq", "op": "=="},
    'ne': {"method_name": "ne", "op": "!="},
    'ge': {"method_name": "ge", "op": ">="},
    'gt': {"method_name": "gt", "op": ">"},
    'le': {"method_name": "le", "op": "<="},
    'lt': {"method_name": "lt", "op": "<"}
}

int_unary_method_info = {
    'pos': {"method_name": "pos", "expr": "py_int_from_host(py_int_to_host(self))"},
    'neg': {"method_name": "neg", "expr": "py_int_from_host(-py_int_to_host(self))"},
    'invert': {"method_name": "invert", "expr": "py_int_from_host(~py_int_to_host(self))"},
}

# ======================================================================================================================
#   bool class templates
# ======================================================================================================================


bool_binary_method_template = \
    """
    def __{method_name}__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return {bool_expr}
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) {int_op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'bool' object but received a '" + type(self).__name__ + "'")
"""

bool_reflected_binary_method_template = \
    """
    def __r{method_name}__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return {bool_expr}
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) {int_op} py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__r{method_name}__' requires a 'bool' object but received a '" + type(self).__name__ + "'")
"""

class_bool_template = \
    """@builtin
class bool(int):
    def __new__(cls, val=absent):
        if cls is bool:
            if val is absent:
                return False
            else:
                return semantics_truth(val)
        else:
            raise TypeError("bool.__new__ expected a subtype of 'bool' as first argument")

    def __repr__(self):
        if self is True:
            return "True"
        elif self is False:
            return "False"
        else:
            raise TypeError("descriptor '__repr__' requires a 'bool' object but received a '" + type(self).__name__ + "'")
{methods}"""

bool_method_info = {
    'bitand': {"method_name": "and",
               "bool_expr": "other if self is True else False",
               "int_op": "&"},
    'bitor': {"method_name": "or",
              "base": "True",
              "bool_expr": "True if self is True else other",
              "int_op": "|"},
    'xor': {"method_name": "xor", "base": "True",
            "bool_expr": "self is not other",
            "int_op": "^"}
}

# ======================================================================================================================
#   float class templates
# ======================================================================================================================


float_binary_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) {op} py_float_to_host(other))
            elif isinstance(other, int):
                return py_float_from_host(py_float_to_host(self) {op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_reflected_binary_method_template = \
    """
    def __r{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(other) {op} py_float_to_host(self))
            elif isinstance(other, int):
                return py_float_from_host(py_int_to_host(other) {op} py_float_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__r{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_inplace_binary_method_template = \
    """
    def __i{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) {op} py_float_to_host(other))
            elif isinstance(self, int):
                return py_float_from_host(py_float_to_host(self) {op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__i{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_division_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) {op} py_float_to_host(other))
                else:
                    raise ZeroDivisionError("{error_message}")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ZeroDivisionError("{error_message}")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_reflected_division_method_template = \
    """
    def __r{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(other) {op} py_float_to_host(self))
                else:
                    raise ZeroDivisionError("{error_message}")
            elif isinstance(other, int):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_int_to_host(other) {op} py_float_to_host(self))
                else:
                    raise ZeroDivisionError("{error_message}")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__r{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_inplace_division_method_template = \
    """
    def __i{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) {op} py_float_to_host(other))
                else:
                    raise ZeroDivisionError("{error_message}")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) {op} py_int_to_host(other))
                else:
                    raise ZeroDivisionError("{error_message}")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__i{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_comparison_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) {op} py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) {op} py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

float_unary_method_template = \
    """
    def __{method_name}__(self):
        if isinstance(self, float):
            return {expr}
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'float' object but received a '" + type(self).__name__ + "'")
"""

class_float_template = \
    """
@builtin
@private
def convert_to_float(obj):
    float_conversion = semantics_maybe_to_float(obj)
    if float_conversion is absent:
        if isinstance(obj, str):
            return str_to_float(obj)
        else:
            raise TypeError("float() argument must be a string or a number, not '" + type(obj).__name__ + "'")
    else:
        return float_conversion

@builtin
@private
def str_to_float(s):
    def err():
        raise ValueError('could not convert string to float: ' + repr(s))
    pos = 0
    end = len(s)
    if pos >= end:
        err()
    after_sign = pos
    c = ord(s[pos])
    pos += 1
    if c == 45 or c == 43:  # '-'/'+' ?
        after_sign = pos
        if pos >= end:
            err()
        c = ord(s[pos])
        pos += 1
    # check for inf and nan
    if c == 105 or c == 73:  # 'i'/'I' ?
        # has to be inf... check all possible cases
        s_lower = s.lower()
        if after_sign == 0:  # no sign?
            if s_lower == 'inf' or s_lower == 'infinity':
                return 1e333  # inf
            else:
                err()
        elif ord(s[0]) == 45:  # '-' sign?
            if s_lower == '-inf' or s_lower == '-infinity':
                return -1e333  # -inf
            else:
                err()
        else:  # '+' sign!
            if s_lower == '+inf' or s_lower == '+infinity':
                return 1e333  # inf
            else:
                err()
    elif c == 110 or c == 78:  # 'n'/'N' ?
        # has to be nan... check all possible cases
        s_lower = s.lower()
        if after_sign == 0:  # no sign?
            if s_lower == 'nan':
                return 1e333-1e333  # nan
            else:
                err()
        elif ord(s[0]) == 45:  # '-' sign?
            if s_lower == '-nan':
                return 1e333-1e333  # nan
            else:
                err()
        else:  # '+' sign!
            if s_lower == '+nan':
                return 1e333-1e333  # nan
            else:
                err()
    digits = 0
    if c >= 48 and c <= 57:  # '0'..'9' ?
        digits = digits*10 + (c-48)
        if pos >= end:
            c = -1  # end-of-string
        else:
            c = ord(s[pos])
            pos += 1
            while c >= 48 and c <= 57 or c == 95:  # '0'..'9'/'_' ?
                if c == 95:  # '_' ?
                    if pos >= end:
                        err()
                    c = ord(s[pos])
                    pos += 1
                    if c >= 48 and c <= 57:  # '0'..'9' ?
                        digits = digits*10 + (c-48)
                        if pos >= end:
                            c = -1  # end-of-string
                            break
                        c = ord(s[pos])
                        pos += 1
                    else:
                        err()
                else:
                    digits = digits*10 + (c-48)
                    if pos >= end:
                        c = -1  # end-of-string
                        break
                    c = ord(s[pos])
                    pos += 1
    power10 = 0
    if c == 46:  # '.' ?
        if pos >= end:
            c = -1  # end-of-string
        else:
            c = ord(s[pos])
            pos += 1
            if c >= 48 and c <= 57:  # '0'..'9' ?
                power10 -= 1
                digits = digits*10 + (c-48)
                if pos >= end:
                    c = -1  # end-of-string
                else:
                    c = ord(s[pos])
                    pos += 1
                    while c >= 48 and c <= 57 or c == 95:  # '0'..'9'/'_' ?
                        power10 -= 1
                        if c == 95:  # '_' ?
                            if pos >= end:
                                err()
                            c = ord(s[pos])
                            pos += 1
                            if c >= 48 and c <= 57:  # '0'..'9' ?
                                digits = digits*10 + (c-48)
                                if pos >= end:
                                    c = -1  # end-of-string
                                    break
                                c = ord(s[pos])
                                pos += 1
                            else:
                                err()
                        else:
                            digits = digits*10 + (c-48)
                            if pos >= end:
                                c = -1  # end-of-string
                                break
                            c = ord(s[pos])
                            pos += 1
        if pos == after_sign+1:
            err()
    if c == 101 or c == 69:  # 'e'/'E' ?
        if pos >= end:
            err()
        c = ord(s[pos])
        pos += 1
        neg_expo = c == 45  # '-' ?
        if neg_expo or c == 43:  # '-'/'+' ?
            if pos >= end:
                err()
            c = ord(s[pos])
            pos += 1
        expo = 0
        if c >= 48 and c <= 57:  # '0'..'9' ?
            expo = expo*10 + (c-48)
            if pos >= end:
                c = -1  # end-of-string
            else:
                c = ord(s[pos])
                pos += 1
                while c >= 48 and c <= 57 or c == 95:  # '0'..'9'/'_' ?
                    if c == 95:  # '_' ?
                        if pos >= end:
                            err()
                        c = ord(s[pos])
                        pos += 1
                        if c >= 48 and c <= 57:  # '0'..'9' ?
                            expo = expo*10 + (c-48)
                            if pos >= end:
                                c = -1  # end-of-string
                                break
                            c = ord(s[pos])
                            pos += 1
                        else:
                            err()
                    else:
                        expo = expo*10 + (c-48)
                        if pos >= end:
                            c = -1  # end-of-string
                            break
                        c = ord(s[pos])
                        pos += 1
            if neg_expo:
                power10 -= expo
            else:
                power10 += expo
        else:
            err()
    if power10 >= 0:
        if power10 > 0:
            digits = digits * (10**power10)
        if digits > 1.7976931348623158e+308:  # avoid int to float overflow
            result = 1e333  # inf
        else:
            result = 1.0 * digits  # convert to float
    else:
        result = digits / (10**-power10)
    if after_sign == 1 and ord(s[0]) == 45:  # '-' sign?
        if result == 0.0:
            result = -0.0  # minus zero
        else:
            result = -result
    return result

@builtin
class float:
    def __new__(cls, val=absent):
        if cls is float:
            if val is absent:
                return 0.0
            else:
                return convert_to_float(val)
        elif isinstance(cls, type) and issubclass(cls, float):
            if val is absent:
                return alloc(float, cls=cls, value=py_float_to_host(0.0))
            else:
                return alloc(float, cls=cls, value=py_float_to_host(convert_to_float(val)))
        else:
            raise TypeError("float.__new__ expected a subtype of 'float' as first argument")

    def __float__(self):
        if isinstance(self, float):
            return py_float_from_host(py_float_to_host(self))
        else:
            raise TypeError("descriptor '__float__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __bool__(self):
        if isinstance(self, float):
            return self != 0.0
        else:
            raise TypeError("descriptor '__bool__' requires a 'float' object but received a '" + type(self).__name__ + "'")
{methods}"""

float_method_info = {
    'add': {"method_name": "add", "op": "+"},
    'mul': {"method_name": "mul", "op": "*"},
    'pow': {"method_name": "pow", "op": "**"},
    'sub': {"method_name": "sub", "op": "-"},
}

float_division_method_info = {
    'floordiv': {"method_name": "floordiv", "op": "//", "error_message": "float division by zero"},
    'truediv': {"method_name": "truediv", "op": "/", "error_message": "float division by zero"},
    'mod': {"method_name": "mod", "op": "%", "error_message": "float modulo by zero"}
}

float_comparison_method_info = {
    'eq': {"method_name": "eq", "op": "=="},
    'ne': {"method_name": "ne", "op": "!="},
    'ge': {"method_name": "ge", "op": ">="},
    'gt': {"method_name": "gt", "op": ">"},
    'le': {"method_name": "le", "op": "<="},
    'lt': {"method_name": "lt", "op": "<"}
}

float_unary_method_info = {
    'pos': {"method_name": "pos", "expr": "self"},
    'neg': {"method_name": "neg", "expr": "py_float_from_host(-py_float_to_host(self))"},
}

# ======================================================================================================================
#   float class templates
# ======================================================================================================================


str_comparison_method_template = \
    """
    def __{method_name}__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) {op} py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__{method_name}__' requires a 'str' object but received a '" + type(self).__name__ + "'")
"""


str_comparison_method_info = {
    'eq': {"method_name": "eq", "op": "=="},
    'ne': {"method_name": "ne", "op": "!="},
    'ge': {"method_name": "ge", "op": ">="},
    'gt': {"method_name": "gt", "op": ">"},
    'le': {"method_name": "le", "op": "<="},
    'lt': {"method_name": "lt", "op": "<"}
}


class_str_template = \
"""@builtin
class str:
    def __len__(self):
        if isinstance(self, str):
            return py_int_from_host(py_str_len_to_host(self))
        else:
            raise TypeError("descriptor '__len__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __add__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_str_from_host(py_str_to_host(self) + py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__add__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __mul__(self, other):
        if isinstance(self, str):
            if isinstance(other, int):
                return py_str_from_host(py_str_to_host(self) * py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__mul__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __rmul__(self, other):
        if isinstance(self, str):
            if isinstance(other, int):
                return py_str_from_host(py_str_to_host(self) * py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rmul__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __mod__(self, values):
        mapping = None
        if isinstance(values, dict):
            mapping = values
        if not isinstance(values, tuple):
            values = (values,)
        result = ''
        start = 0
        end = len(self)
        value_index = 0
        pos = start
        while pos < end:
            c = self[pos]
            pos += 1
            if c == '%':
                if pos >= end:
                    raise ValueError('incomplete format')
                else:
                    c = self[pos]
                    pos += 1
                    if c == '%':
                        result += self[start:pos-1]
                        start = pos
                    else:
                        result += self[start:pos-2]
                        if c == '(':
                            if mapping is None:
                                raise TypeError('format requires a mapping')
                            value_index = 1
                            key_start = pos
                            while pos < end and self[pos] != ')':
                                pos += 1
                            if pos >= end:
                                raise ValueError('incomplete format key')
                            key = self[key_start:pos]
                            pos += 1
                            if pos >= end:
                                raise ValueError('incomplete format')
                            else:
                                c = self[pos]
                                pos += 1
                            value = mapping[key] # ok if this raises a KeyError
                        else:
                            if value_index >= len(values):
                                raise TypeError('not enough arguments for format string')
                            else:
                                value = values[value_index]
                                value_index += 1
                        flag_zero  = False
                        flag_minus = False
                        flag_plus  = False
                        flag_space = False
                        flag_alt   = False
                        while c == '0' or c == '-' or c == '+' or c == ' ' or c == '#':
                            if c == '0':
                                flag_zero  = True
                            elif c == '-':
                                flag_minus = True
                            elif c == '+':
                                flag_plus  = True
                            elif c == ' ':
                                flag_space = True
                            else:
                                flag_alt   = True
                            if pos >= end:
                                raise ValueError('incomplete format')
                            else:
                                c = self[pos]
                                pos += 1
                        width = 0
                        while c >= '0' and c <= '9':
                            width = width*10 + (ord(c) - 48)
                            if pos >= end:
                                raise ValueError('incomplete format')
                            else:
                                c = self[pos]
                                pos += 1
                        start = pos
                        def output(s):
                            nonlocal result
                            n = len(s)
                            if width <= n:
                                result += s
                            elif flag_minus:
                                result += s + ' '*(width-n)
                            else:
                                result += ' '*(width-n) + s
                        if c == 's' or c == 'r' or c == 'a':
                            if c == 's':
                                output(str(value))
                            elif c == 'r':
                                output(repr(value))
                            elif c == 'a':
                                output(ascii(value))
                        elif c == 'i' or c == 'd' or c == 'u' or c == 'o' or c == 'x' or c == 'X':
                            # TODO: handle flags and different formats
                            output(str(value))
                        elif c == 'e' or c == 'E' or c == 'f' or c == 'F' or c == 'g' or c == 'G':
                            # TODO: handle flags and different formats
                            output(str(value))
                        elif c == 'c':
                            if isinstance(value, int):
                                output(chr(value))
                            elif isinstance(value, str) and len(value) == 1:
                                output(value)
                            else:
                                raise TypeError('%c requires int or char')
                        else:
                            n = ord(c)
                            raise ValueError('unsupported format character ' + repr(c if n>=32 and n<=126 else '?') + ' (' + hex(n) + ') at index ' + str(pos-1))
        if mapping is None and value_index != len(values):
            raise TypeError('not all arguments converted during string formating')
        if start < pos:
            result += self[start:pos]
        return result
{methods}
"""


# ======================================================================================================================
#   builtins class templates
# =====================================================================================================================


builtins_template = """\
from __compiler_intrinsics__ import absent, builtin, private, alloc, py_int_from_host, py_int_to_host, py_float_from_host, py_float_to_host, py_bool_from_host_bool, py_bool_to_host_bool, py_str_to_host, py_str_from_host, py_str_len_to_host, semantics_truth, semantics_maybe_to_int, semantics_maybe_to_float, semantics_maybe_index, semantics_maybe_trunc, semantics_big_index


@builtin
class staticmethod:
    def __new__(cls, obj):
        if cls is staticmethod:
            return alloc(staticmethod, method=obj)
        elif isinstance(cls, staticmethod):
            return alloc(staticmethod, cls=cls, method=obj)
        else:
            raise TypeError("staticmethod.__new__ expected a subtype of 'staticmethod' as first argument")

    def __get__(self, instance, owner=None):
        if isinstance(self, staticmethod):
            return self.method
        else:
            raise TypeError("descriptor '__get__' requires a 'staticmethod' object but received a '" + type(self).__name__ + "'")


@private
@builtin
class method:
    def __new__(cls, method_, self):
        if cls is method:
            alloc(method, method=method_, self=self)
        else:
            raise TypeError("method.__new__ expected a subtype of 'method' as first argument")

    def __call__(self, *args, **kwargs):
        return self.method(self.self, *args, **kwargs)


@private
@builtin
class function:
    def __new__(cls, code, glo):
        if cls is function:
            raise NotImplementedError
        else:
            raise TypeError("function.__new__ expected a subtype of 'function' as first argument")

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return alloc(method, method=self, self=instance)


@builtin
class classmethod:
    def __new__(cls, obj):
        if cls is classmethod:
            return alloc(classmethod, method=obj)
        elif isinstance(cls, classmethod):
            return alloc(classmethod, cls=cls, method=obj)
        else:
            raise TypeError("classmethod.__new__ expected a subtype of 'classmethod' as first argument")

    def __get__(self, instance, owner=None):
        if isinstance(self, classmethod):
            if owner is None:
                return alloc(method, method=self.method, self=type(instance))
            else:
                return alloc(method, method=self.method, self=owner)
        else:
            raise TypeError("descriptor '__get__' requires a 'classmethod' object but received a '" + type(self).__name__ + "'")

{definitions}

@builtin
@private
class range_iterator:
    def __new__(*args):
        raise ValueError("cannot create 'range_iterator' instances")

    def __iter__(self, /):
        return self

    def __next__(self, /):
        start = self.start
        stop = self.stop
        step = self.step

        if step < 0:
            if start > stop:
                self.start = start + step
                return start
            else:
                raise StopIteration
        else:
            if start < stop:
                self.start = start + step
                return start
            else:
                raise StopIteration

@builtin
class range:
    def __new__(cls, arg1, arg2=absent, arg3=absent, /):
        if cls is range:
            if arg3 is not absent:
                return alloc(range, start=semantics_big_index(arg1), stop=semantics_big_index(arg2), step=semantics_big_index(arg3))
            elif arg2 is not absent:
                return alloc(range, start=semantics_big_index(arg1), stop=semantics_big_index(arg2), step=1)
            else:
                return alloc(range, start=0, stop=semantics_big_index(arg1), step=1)
        else:
            raise TypeError("range.__new__ expected a subtype of 'range' as first argument")

    def __len__(self, /):
        return (self.stop - self.start) // self.step

    def __contains__(self, item, /):
        start = self.start
        stop = self.stop
        step = self.step

        if step < 0:
            if stop >= item or item > start:
                return False
        else:
            if start > item or item >= stop:
                return False

        return (item - start) % step == 0

    def __iter__(self, /):
        return alloc(range_iterator, start=self.start, stop=self.stop, step=self.step)

    def __repr__(self):
        start = self.start
        stop = self.stop
        step = self.step

        if step == 1:
            return "range(" + str(start) + ", " + str(stop) + ")"
        else:
            return "range(" + str(start) + ", " + str(stop) + ", " + str(step) + ")"

@private
@builtin
def __merge(l1, l2):
    \"""
    Merge all items from two sorted list into one sorted list.
    Time complexity: O(n) where n is the total number of elements
    \"""
    i = j = 0
    output = []

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            output.append(l1[i])
            i += 1
        else:
            output.append(l2[j])
            j += 1

    output.extend(l1[i:] + l2[j:])

    return output

@private
@builtin
def __merge_many(lsts):
    \"""
    Merge all items from k lists into one sorted list.
    Time complexity: O(n log(k)) where n is the total number of elements and k the number of lists
    \"""
    if not lsts:
        return []
    elif len(lsts) == 1:
        return lsts[0][:]
    elif len(lsts) == 2:
        return __merge(lsts[0], lsts[1])
    else:
        left = lsts[len(lsts) // 2:]
        right = lsts[:len(lsts) // 2]

        return __merge(__merge_many(left), __merge_many(right))


# TODO: key and reversed must be kwonlyargs
@builtin
def sorted(lst, key=None, reversed=False):
    \"""
    Timsort is an improved version of Merge Sort which splits the list into monotonic sub-lists before merging them
    into a sorted list.
    Worst case time complexity: O(n log(n))
    Best cast time complexity:  O(n) when the list is almost sorted
        where n is the number of elements in the list
    \"""
    sublsts = []

    i = 0
    while i < len(lst):
        sublsts.append([lst[i]])
        i += 1

        if i < len(lst) and lst[i] >= lst[i - 1]:
            while i < len(lst) and lst[i] >= lst[i - 1]:
                sublsts[-1].append(lst[i])
                i += 1
        elif i < len(lst):
            while i < len(lst) and lst[i] < lst[i - 1]:
                sublsts[-1].append(lst[i])
                i += 1

            sublsts[-1] = sublsts[-1][::-1]

    return __merge_many(sublsts)

# ==============================================================================
# Exceptions
# ==============================================================================

@builtin
class BaseException:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        args = self.args
        args_len = len(self.args)

        if args_len == 0:
            return ""
        elif args_len == 1:
            return str(args[0])
        else:
            return str(args)

@builtin
class Exception(BaseException):
    pass

@builtin
class GeneratorExit(BaseException):
    pass


@builtin
class KeyboardInterrupt(BaseException):
    pass


@builtin
class SystemExit(BaseException):
    pass


@builtin
class ArithmeticError(Exception):
    pass


@builtin
class AssertionError(Exception):
    pass


@builtin
class AttributeError(Exception):
    pass


@builtin
class BufferError(Exception):
    pass


@builtin
class EOFError(Exception):
    pass


@builtin
class ImportError(Exception):
    pass


@builtin
class LookupError(Exception):
    pass


@builtin
class MemoryError(Exception):
    pass


@builtin
class NameError(Exception):
    pass


@builtin
class EnvironmentError(Exception):
    pass


@builtin
class IOError(Exception):
    pass


@builtin
class OSError(Exception):
    pass


@builtin
class ReferenceError(Exception):
    pass


@builtin
class RuntimeError(Exception):
    pass


@builtin
class StopAsyncIteration(Exception):
    pass


@builtin
class StopIteration(Exception):
    pass


@builtin
class SyntaxError(Exception):
    pass


@builtin
class SystemError(Exception):
    pass


@builtin
class TypeError(Exception):
    pass


@builtin
class ValueError(Exception):
    pass


@builtin
class Warning(Exception):
    pass


@builtin
class FloatingPointError(ArithmeticError):
    pass


@builtin
class OverflowError(ArithmeticError):
    pass


@builtin
class ZeroDivisionError(ArithmeticError):
    pass


@builtin
class ModuleNotFoundError(ImportError):
    pass


@builtin
class IndexError(LookupError):
    pass


@builtin
class KeyError(LookupError):
    pass


@builtin
class UnboundLocalError(NameError):
    pass


@builtin
class BlockingIOError(OSError):
    pass


@builtin
class ChildProcessError(OSError):
    pass


@builtin
class ConnectionError(OSError):
    pass


@builtin
class FileExistsError(OSError):
    pass


@builtin
class FileNotFoundError(OSError):
    pass


@builtin
class InterruptedError(OSError):
    pass


@builtin
class IsADirectoryError(OSError):
    pass


@builtin
class NotADirectoryError(OSError):
    pass


@builtin
class PermissionError(OSError):
    pass


@builtin
class ProcessLookupError(OSError):
    pass


@builtin
class TimeoutError(OSError):
    pass


@builtin
class NotImplementedError(RuntimeError):
    pass


@builtin
class RecursionError(RuntimeError):
    pass


@builtin
class IndentationError(SyntaxError):
    pass


@builtin
class UnicodeError(ValueError):
    pass


@builtin
class BytesWarning(Warning):
    pass


@builtin
class DeprecationWarning(Warning):
    pass


@builtin
class FutureWarning(Warning):
    pass


@builtin
class ImportWarning(Warning):
    pass


@builtin
class PendingDeprecationWarning(Warning):
    pass


@builtin
class ResourceWarning(Warning):
    pass


@builtin
class RuntimeWarning(Warning):
    pass


@builtin
class SyntaxWarning(Warning):
    pass


@builtin
class UnicodeWarning(Warning):
    pass


@builtin
class UserWarning(Warning):
    pass


@builtin
class BrokenPipeError(ConnectionError):
    pass


@builtin
class ConnectionAbortedError(ConnectionError):
    pass


@builtin
class ConnectionRefusedError(ConnectionError):
    pass


@builtin
class ConnectionResetError(ConnectionError):
    pass


@builtin
class TabError(IndentationError):
    pass


@builtin
class UnicodeDecodeError(UnicodeError):
    pass


@builtin
class UnicodeEncodeError(UnicodeError):
    pass


@builtin
class UnicodeTranslateError(UnicodeError):
    pass
"""
