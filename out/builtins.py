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

    def __add__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) + py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__add__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __radd__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) + py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__radd__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __iadd__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) + py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__iadd__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __and__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) & py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__and__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rand__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) & py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rand__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __iand__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) & py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__iand__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __or__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) | py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__or__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ror__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) | py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ror__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ior__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) | py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ior__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __mul__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) * py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__mul__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rmul__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) * py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rmul__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __imul__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) * py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__imul__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __pow__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) ** py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__pow__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rpow__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) ** py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rpow__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ipow__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) ** py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ipow__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __sub__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) - py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__sub__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rsub__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) - py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rsub__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __isub__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) - py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__isub__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __xor__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) ^ py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__xor__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rxor__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) ^ py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rxor__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ixor__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) ^ py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ixor__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __lshift__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) << py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__lshift__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rlshift__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) << py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rlshift__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ilshift__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) << py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ilshift__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rshift__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) >> py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rshift__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rrshift__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) >> py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rrshift__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __irshift__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) >= py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) >> py_int_to_host(other))
                else:
                    raise ValueError("negative shift count")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__irshift__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __pos__(self):
        if isinstance(self, int):
            return py_int_from_host(py_int_to_host(self))
        else:
            raise TypeError("descriptor '__pos__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __neg__(self):
        if isinstance(self, int):
            return py_int_from_host(-py_int_to_host(self))
        else:
            raise TypeError("descriptor '__neg__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __invert__(self):
        if isinstance(self, int):
            return py_int_from_host(~py_int_to_host(self))
        else:
            raise TypeError("descriptor '__invert__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __floordiv__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) // py_int_to_host(other))
                else:
                    raise ZeroDivisionError("integer division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__floordiv__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rfloordiv__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) != py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(other) // py_int_to_host(self))
                else:
                    raise ZeroDivisionError("integer division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rfloordiv__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ifloordiv__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) // py_int_to_host(other))
                else:
                    raise ZeroDivisionError("integer division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ifloordiv__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __truediv__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_int_to_host(self) / py_int_to_host(other))
                else:
                    raise ZeroDivisionError("division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__truediv__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rtruediv__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) != py_int_to_host(0):
                    return py_float_from_host(py_int_to_host(other) / py_int_to_host(self))
                else:
                    raise ZeroDivisionError("division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rtruediv__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __itruediv__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_int_to_host(self) / py_int_to_host(other))
                else:
                    raise ZeroDivisionError("division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__itruediv__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __mod__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) % py_int_to_host(other))
                else:
                    raise ZeroDivisionError("modulo by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__mod__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __rmod__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(self) != py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(other) % py_int_to_host(self))
                else:
                    raise ZeroDivisionError("modulo by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rmod__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __imod__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_int_from_host(py_int_to_host(self) % py_int_to_host(other))
                else:
                    raise ZeroDivisionError("modulo by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__imod__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __eq__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) == py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__eq__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ne__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) != py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ne__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __ge__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) >= py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ge__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __gt__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) > py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__gt__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __le__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) <= py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__le__' requires a 'int' object but received a '" + type(self).__name__ + "'")

    def __lt__(self, other):
        if isinstance(self, int):
            if isinstance(other, int):
                return py_bool_from_host_bool(py_int_to_host(self) < py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__lt__' requires a 'int' object but received a '" + type(self).__name__ + "'")


@builtin
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

    def __and__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return other if self is True else False
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) & py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__and__' requires a 'bool' object but received a '" + type(self).__name__ + "'")

    def __rand__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return other if self is True else False
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) & py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rand__' requires a 'bool' object but received a '" + type(self).__name__ + "'")

    def __or__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return True if self is True else other
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) | py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__or__' requires a 'bool' object but received a '" + type(self).__name__ + "'")

    def __ror__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return True if self is True else other
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) | py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ror__' requires a 'bool' object but received a '" + type(self).__name__ + "'")

    def __xor__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return self is not other
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(self) ^ py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__xor__' requires a 'bool' object but received a '" + type(self).__name__ + "'")

    def __rxor__(self, other):
        if type(self) is bool:
            if type(other) is bool:
                return self is not other
            elif isinstance(other, int):
                return py_int_from_host(py_int_to_host(other) ^ py_int_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rxor__' requires a 'bool' object but received a '" + type(self).__name__ + "'")



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

    def __add__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) + py_float_to_host(other))
            elif isinstance(other, int):
                return py_float_from_host(py_float_to_host(self) + py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__add__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __radd__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(other) + py_float_to_host(self))
            elif isinstance(other, int):
                return py_float_from_host(py_int_to_host(other) + py_float_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__radd__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __iadd__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) + py_float_to_host(other))
            elif isinstance(self, int):
                return py_float_from_host(py_float_to_host(self) + py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__iadd__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __mul__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) * py_float_to_host(other))
            elif isinstance(other, int):
                return py_float_from_host(py_float_to_host(self) * py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__mul__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __rmul__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(other) * py_float_to_host(self))
            elif isinstance(other, int):
                return py_float_from_host(py_int_to_host(other) * py_float_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rmul__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __imul__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) * py_float_to_host(other))
            elif isinstance(self, int):
                return py_float_from_host(py_float_to_host(self) * py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__imul__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __pow__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) ** py_float_to_host(other))
            elif isinstance(other, int):
                return py_float_from_host(py_float_to_host(self) ** py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__pow__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __rpow__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(other) ** py_float_to_host(self))
            elif isinstance(other, int):
                return py_float_from_host(py_int_to_host(other) ** py_float_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rpow__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __ipow__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) ** py_float_to_host(other))
            elif isinstance(self, int):
                return py_float_from_host(py_float_to_host(self) ** py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ipow__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __sub__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) - py_float_to_host(other))
            elif isinstance(other, int):
                return py_float_from_host(py_float_to_host(self) - py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__sub__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __rsub__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(other) - py_float_to_host(self))
            elif isinstance(other, int):
                return py_float_from_host(py_int_to_host(other) - py_float_to_host(self))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rsub__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __isub__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_float_from_host(py_float_to_host(self) - py_float_to_host(other))
            elif isinstance(self, int):
                return py_float_from_host(py_float_to_host(self) - py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__isub__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __pos__(self):
        if isinstance(self, float):
            return self
        else:
            raise TypeError("descriptor '__pos__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __neg__(self):
        if isinstance(self, float):
            return py_float_from_host(-py_float_to_host(self))
        else:
            raise TypeError("descriptor '__neg__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __floordiv__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) // py_float_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) // py_int_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__floordiv__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __rfloordiv__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(other) // py_float_to_host(self))
                else:
                    raise ZeroDivisionError("float division by zero")
            elif isinstance(other, int):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_int_to_host(other) // py_float_to_host(self))
                else:
                    raise ZeroDivisionError("float division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rfloordiv__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __ifloordiv__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) // py_float_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) // py_int_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ifloordiv__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __truediv__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) / py_float_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) / py_int_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__truediv__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __rtruediv__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(other) / py_float_to_host(self))
                else:
                    raise ZeroDivisionError("float division by zero")
            elif isinstance(other, int):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_int_to_host(other) / py_float_to_host(self))
                else:
                    raise ZeroDivisionError("float division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rtruediv__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __itruediv__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) / py_float_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) / py_int_to_host(other))
                else:
                    raise ZeroDivisionError("float division by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__itruediv__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __mod__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) % py_float_to_host(other))
                else:
                    raise ZeroDivisionError("float modulo by zero")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) % py_int_to_host(other))
                else:
                    raise ZeroDivisionError("float modulo by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__mod__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __rmod__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(other) % py_float_to_host(self))
                else:
                    raise ZeroDivisionError("float modulo by zero")
            elif isinstance(other, int):
                if py_float_to_host(self) != py_float_to_host(0.0):
                    return py_float_from_host(py_int_to_host(other) % py_float_to_host(self))
                else:
                    raise ZeroDivisionError("float modulo by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__rmod__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __imod__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                if py_float_to_host(other) != py_float_to_host(0.0):
                    return py_float_from_host(py_float_to_host(self) % py_float_to_host(other))
                else:
                    raise ZeroDivisionError("float modulo by zero")
            elif isinstance(other, int):
                if py_int_to_host(other) != py_int_to_host(0):
                    return py_float_from_host(py_float_to_host(self) % py_int_to_host(other))
                else:
                    raise ZeroDivisionError("float modulo by zero")
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__imod__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __eq__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) == py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) == py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__eq__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __ne__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) != py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) != py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ne__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __ge__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) >= py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) >= py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ge__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __gt__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) > py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) > py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__gt__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __le__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) <= py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) <= py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__le__' requires a 'float' object but received a '" + type(self).__name__ + "'")

    def __lt__(self, other):
        if isinstance(self, float):
            if isinstance(other, float):
                return py_bool_from_host_bool(py_float_to_host(self) < py_float_to_host(other))
            elif isinstance(other, int):
                return py_bool_from_host_bool(py_float_to_host(self) < py_int_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__lt__' requires a 'float' object but received a '" + type(self).__name__ + "'")


@builtin
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

    def __eq__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) == py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__eq__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __ne__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) != py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ne__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __ge__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) >= py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__ge__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __gt__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) > py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__gt__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __le__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) <= py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__le__' requires a 'str' object but received a '" + type(self).__name__ + "'")

    def __lt__(self, other):
        if isinstance(self, str):
            if isinstance(other, str):
                return py_bool_from_host_bool(py_str_to_host(self) < py_str_to_host(other))
            else:
                return NotImplemented
        else:
            raise TypeError("descriptor '__lt__' requires a 'str' object but received a '" + type(self).__name__ + "'")



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
    """
    Merge all items from two sorted list into one sorted list.
    Time complexity: O(n) where n is the total number of elements
    """
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
    """
    Merge all items from k lists into one sorted list.
    Time complexity: O(n log(k)) where n is the total number of elements and k the number of lists
    """
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
    """
    Timsort is an improved version of Merge Sort which splits the list into monotonic sub-lists before merging them
    into a sorted list.
    Worst case time complexity: O(n log(n))
    Best cast time complexity:  O(n) when the list is almost sorted
        where n is the number of elements in the list
    """
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
