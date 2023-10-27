from __compiler_intrinsics__ import define_semantics, class_getattr, mro_lookup, py_bool_to_host_bool, absent, sint, bint

# Auto-generated
@define_semantics
def add(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__add__")
    y_method = mro_lookup(y_type, "__radd__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("+", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("+", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("+", x, y)

    return result

# Auto-generated
@define_semantics
def bitand(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__and__")
    y_method = mro_lookup(y_type, "__rand__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("&", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("&", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("&", x, y)

    return result

# Auto-generated
@define_semantics
def bitor(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__or__")
    y_method = mro_lookup(y_type, "__ror__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("|", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("|", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("|", x, y)

    return result

# Auto-generated
@define_semantics
def floordiv(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__floordiv__")
    y_method = mro_lookup(y_type, "__rfloordiv__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("//", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("//", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("//", x, y)

    return result

# Auto-generated
@define_semantics
def lshift(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__lshift__")
    y_method = mro_lookup(y_type, "__rlshift__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("<<", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("<<", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("<<", x, y)

    return result

# Auto-generated
@define_semantics
def matmul(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__matmul__")
    y_method = mro_lookup(y_type, "__rmatmul__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("@", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("@", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("@", x, y)

    return result

# Auto-generated
@define_semantics
def mod(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__mod__")
    y_method = mro_lookup(y_type, "__rmod__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("%", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("%", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("%", x, y)

    return result

# Auto-generated
@define_semantics
def mul(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__mul__")
    y_method = mro_lookup(y_type, "__rmul__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("*", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("*", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("*", x, y)

    return result

# Auto-generated
@define_semantics
def pow(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__pow__")
    y_method = mro_lookup(y_type, "__rpow__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("**", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("**", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("**", x, y)

    return result

# Auto-generated
@define_semantics
def rshift(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__rshift__")
    y_method = mro_lookup(y_type, "__rrshift__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError(">>", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError(">>", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError(">>", x, y)

    return result

# Auto-generated
@define_semantics
def sub(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__sub__")
    y_method = mro_lookup(y_type, "__rsub__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("-", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("-", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("-", x, y)

    return result

# Auto-generated
@define_semantics
def truediv(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__truediv__")
    y_method = mro_lookup(y_type, "__rtruediv__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("/", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("/", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("/", x, y)

    return result

# Auto-generated
@define_semantics
def xor(x, y):
    def normal():
        if x_method is absent:
            return NotImplemented
        else:
            return x_method(x, y)

    def reflected():
        if y_method is absent:
            return NotImplemented
        else:
            return y_method(y, x)

    x_type = type(x)
    y_type = type(y)

    x_method = mro_lookup(x_type, "__xor__")
    y_method = mro_lookup(y_type, "__rxor__")

    if x_type is y_type:
        result = normal()
        if result is NotImplemented:
            return raise_binary_TypeError("^", x, y)
    elif issubclass(x_type, y_type) and x_method is not y_method:
        result = reflected()
        if result is NotImplemented:
            result = normal()
            if result is NotImplemented:
                return raise_binary_TypeError("^", x, y)
    else:
        result = normal()
        if result is NotImplemented:
            result = reflected()
            if result is NotImplemented:
                return raise_binary_TypeError("^", x, y)

    return result

# Auto-generated
@define_semantics
def iadd(x, y):
    def inplace():
        magic_method = class_getattr(x, "__iadd__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__add__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__radd__")
        if magic_method is absent:
            return raise_binary_TypeError("+=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("+=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def ibitand(x, y):
    def inplace():
        magic_method = class_getattr(x, "__iand__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__and__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rand__")
        if magic_method is absent:
            return raise_binary_TypeError("&=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("&=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def ibitor(x, y):
    def inplace():
        magic_method = class_getattr(x, "__ior__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__or__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__ror__")
        if magic_method is absent:
            return raise_binary_TypeError("|=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("|=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def ifloordiv(x, y):
    def inplace():
        magic_method = class_getattr(x, "__ifloordiv__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__floordiv__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rfloordiv__")
        if magic_method is absent:
            return raise_binary_TypeError("//=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("//=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def ilshift(x, y):
    def inplace():
        magic_method = class_getattr(x, "__ilshift__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__lshift__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rlshift__")
        if magic_method is absent:
            return raise_binary_TypeError("<<=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("<<=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def imatmul(x, y):
    def inplace():
        magic_method = class_getattr(x, "__imatmul__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__matmul__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rmatmul__")
        if magic_method is absent:
            return raise_binary_TypeError("@=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("@=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def imod(x, y):
    def inplace():
        magic_method = class_getattr(x, "__imod__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__mod__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rmod__")
        if magic_method is absent:
            return raise_binary_TypeError("%=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("%=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def imul(x, y):
    def inplace():
        magic_method = class_getattr(x, "__imul__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__mul__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rmul__")
        if magic_method is absent:
            return raise_binary_TypeError("*=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("*=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def ipow(x, y):
    def inplace():
        magic_method = class_getattr(x, "__ipow__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__pow__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rpow__")
        if magic_method is absent:
            return raise_binary_TypeError("**=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("**=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def irshift(x, y):
    def inplace():
        magic_method = class_getattr(x, "__irshift__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__rshift__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rrshift__")
        if magic_method is absent:
            return raise_binary_TypeError(">>=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError(">>=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def isub(x, y):
    def inplace():
        magic_method = class_getattr(x, "__isub__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__sub__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rsub__")
        if magic_method is absent:
            return raise_binary_TypeError("-=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("-=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def itruediv(x, y):
    def inplace():
        magic_method = class_getattr(x, "__itruediv__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__truediv__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rtruediv__")
        if magic_method is absent:
            return raise_binary_TypeError("/=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("/=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def ixor(x, y):
    def inplace():
        magic_method = class_getattr(x, "__ixor__")
        if magic_method is absent:
            return normal()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return normal()
            else:
                return result

    def normal():
        magic_method = class_getattr(x, "__xor__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__rxor__")
        if magic_method is absent:
            return raise_binary_TypeError("^=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("^=", x, y)
            else:
                return result

    return inplace()

# Auto-generated
@define_semantics
def pos(x):
    def normal():
        magic_method = class_getattr(x, "__pos__")
        if magic_method is absent:
            return raise_unary_TypeError("+", x)
        else:
            return magic_method(x)

    return normal()

# Auto-generated
@define_semantics
def neg(x):
    def normal():
        magic_method = class_getattr(x, "__neg__")
        if magic_method is absent:
            return raise_unary_TypeError("-", x)
        else:
            return magic_method(x)

    return normal()

# Auto-generated
@define_semantics
def invert(x):
    def normal():
        magic_method = class_getattr(x, "__invert__")
        if magic_method is absent:
            return raise_unary_TypeError("~", x)
        else:
            return magic_method(x)

    return normal()

# Auto-generated
@define_semantics
def ge(x, y):
    def normal():
        magic_method = class_getattr(x, "__ge__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__le__")
        if magic_method is absent:
            return raise_binary_TypeError(">=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError(">=", x, y)
            else:
                return result

    return normal()

# Auto-generated
@define_semantics
def gt(x, y):
    def normal():
        magic_method = class_getattr(x, "__gt__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__lt__")
        if magic_method is absent:
            return raise_binary_TypeError(">", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError(">", x, y)
            else:
                return result

    return normal()

# Auto-generated
@define_semantics
def le(x, y):
    def normal():
        magic_method = class_getattr(x, "__le__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__ge__")
        if magic_method is absent:
            return raise_binary_TypeError("<=", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("<=", x, y)
            else:
                return result

    return normal()

# Auto-generated
@define_semantics
def lt(x, y):
    def normal():
        magic_method = class_getattr(x, "__lt__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__gt__")
        if magic_method is absent:
            return raise_binary_TypeError("<", x, y)
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return raise_binary_TypeError("<", x, y)
            else:
                return result

    return normal()

# Auto-generated
@define_semantics
def eq(x, y):
    def normal():
        magic_method = class_getattr(x, "__eq__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__eq__")
        if magic_method is absent:
            return default()
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return default()
            else:
                return result

    def default():
        return x is y

    return normal()

# Auto-generated
@define_semantics
def ne(x, y):
    def normal():
        magic_method = class_getattr(x, "__ne__")
        if magic_method is absent:
            return reflected()
        else:
            result = magic_method(x, y)
            if result is NotImplemented:
                return reflected()
            else:
                return result

    def reflected():
        magic_method = class_getattr(y, "__ne__")
        if magic_method is absent:
            return default()
        else:
            result = magic_method(y, x)
            if result is NotImplemented:
                return default()
            else:
                return result

    def default():
        return x is not y

    return normal()

@define_semantics
def raise_binary_TypeError(op, x, y):
    raise TypeError("'"
                    + op
                    + "' not supported between instances of '"
                    + class_getattr(x, "__name__")
                    + "' and '"
                    + class_getattr(y, "__name__")
                    + "'")

@define_semantics
def raise_unary_TypeError(op, x):
    raise TypeError("bad operand type for unary "
                    + op
                    + ":'"
                    + class_getattr(x, "__name__")
                    + "'")

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
            raise TypeError("__trunc__ returned non-int type: '" + class_getattr(obj, "__name__") + "'")

@define_semantics
def trunc(obj):
    result = maybe_trunc(obj)
    if result is absent:
        raise TypeError("type '" + class_getattr(obj, "__name__") + "' doesn't define __trunc__ method")
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
            raise TypeError("__int__ returned non-int type: '" + class_getattr(obj, "__name__") + "'")

@define_semantics
def to_int(obj):
    result = maybe_to_int(obj)
    if result is absent:
        raise TypeError("'" + class_getattr(obj, "__name__") + "' object cannot be interpreted as an integer")
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
            raise TypeError("__float__ returned non-float type: '" + class_getattr(obj, "__name__") + "'")

@define_semantics
def to_float(obj):
    result = maybe_to_float(obj)
    if result is absent:
        raise TypeError("'" + class_getattr(obj, "__name__") + "' object cannot be interpreted as a float")
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
            raise TypeError("__index__ returned non-int type: '" + class_getattr(obj, "__name__") + "'")

@define_semantics
def index(obj):
    result = maybe_index(obj)
    if result is absent:
        raise TypeError("'" + class_getattr(obj, "__name__") + "' object cannot be interpreted as an integer")
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
            raise TypeError("__index__ returned non-int type: '" + class_getattr(obj, "__name__") + "'")

@define_semantics
def big_index(obj):
    result = maybe_big_index(obj)
    if result is absent:
        raise TypeError("'" + class_getattr(obj, "__name__") + "' object cannot be interpreted as an integer")
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
        raise TypeError("object of type" + class_getattr(obj, "__name__") + "has no len()")
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
            raise TypeError("__bool__ should return bool, returned '" + class_getattr(obj, "__name__") + "'")
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
        return __get__(attr, instance, owner)