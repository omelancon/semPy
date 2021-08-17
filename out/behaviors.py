from __compiler_intrinsics__ import define_behavior, sint, bint, py_int_to_float, py_int_from_host, py_int_to_host, py_float_from_host, py_float_to_host, py_sint_to_host, py_bint_to_host, py_bool_from_host_bool, py_bool_to_host_bool, py_str_from_host, py_str_to_host, py_str_len_to_host, alloc

@define_behavior
def py_add_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) + py_float_to_host(y))

@define_behavior
def py_add_sintX_strY(x: sint, y: str):
    raise TypeError("'+' not supported between instances of 'int' and 'str'")

@define_behavior
def py_add_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) + py_float_to_host(y))

@define_behavior
def py_add_bintX_strY(x: bint, y: str):
    raise TypeError("'+' not supported between instances of 'int' and 'str'")

@define_behavior
def py_add_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) + py_float_to_host(y))

@define_behavior
def py_add_boolX_strY(x: bool, y: str):
    raise TypeError("'+' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_add_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) + py_int_to_host(y))

@define_behavior
def py_add_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) + py_float_to_host(y))

@define_behavior
def py_add_floatX_strY(x: float, y: str):
    raise TypeError("'+' not supported between instances of 'float' and 'str'")

@define_behavior
def py_add_strX_sintY(x: str, y: sint):
    raise TypeError("'+' not supported between instances of 'str' and 'int'")

@define_behavior
def py_add_strX_bintY(x: str, y: bint):
    raise TypeError("'+' not supported between instances of 'str' and 'int'")

@define_behavior
def py_add_strX_boolY(x: str, y: bool):
    raise TypeError("'+' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_add_strX_floatY(x: str, y: float):
    raise TypeError("'+' not supported between instances of 'str' and 'float'")

@define_behavior
def py_add_strX_strY(x: str, y: str):
    return py_str_from_host(py_str_to_host(x) + py_str_to_host(y))

@define_behavior
def py_bitand_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_sintX_floatY(x: sint, y: float):
    raise TypeError("'&' not supported between instances of 'int' and 'float'")

@define_behavior
def py_bitand_sintX_strY(x: sint, y: str):
    raise TypeError("'&' not supported between instances of 'int' and 'str'")

@define_behavior
def py_bitand_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_bintX_floatY(x: bint, y: float):
    raise TypeError("'&' not supported between instances of 'int' and 'float'")

@define_behavior
def py_bitand_bintX_strY(x: bint, y: str):
    raise TypeError("'&' not supported between instances of 'int' and 'str'")

@define_behavior
def py_bitand_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_bitand_boolX_boolY(x: bool, y: bool):
    return y if x is True else False

@define_behavior
def py_bitand_boolX_floatY(x: bool, y: float):
    raise TypeError("'&' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_bitand_boolX_strY(x: bool, y: str):
    raise TypeError("'&' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_bitand_floatX_sintY(x: float, y: sint):
    raise TypeError("'&' not supported between instances of 'float' and 'int'")

@define_behavior
def py_bitand_floatX_bintY(x: float, y: bint):
    raise TypeError("'&' not supported between instances of 'float' and 'int'")

@define_behavior
def py_bitand_floatX_boolY(x: float, y: bool):
    raise TypeError("'&' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_bitand_floatX_floatY(x: float, y: float):
    raise TypeError("'&' not supported between instances of 'float' and 'float'")

@define_behavior
def py_bitand_floatX_strY(x: float, y: str):
    raise TypeError("'&' not supported between instances of 'float' and 'str'")

@define_behavior
def py_bitand_strX_sintY(x: str, y: sint):
    raise TypeError("'&' not supported between instances of 'str' and 'int'")

@define_behavior
def py_bitand_strX_bintY(x: str, y: bint):
    raise TypeError("'&' not supported between instances of 'str' and 'int'")

@define_behavior
def py_bitand_strX_boolY(x: str, y: bool):
    raise TypeError("'&' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_bitand_strX_floatY(x: str, y: float):
    raise TypeError("'&' not supported between instances of 'str' and 'float'")

@define_behavior
def py_bitand_strX_strY(x: str, y: str):
    raise TypeError("'&' not supported between instances of 'str' and 'str'")

@define_behavior
def py_bitor_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_sintX_floatY(x: sint, y: float):
    raise TypeError("'|' not supported between instances of 'int' and 'float'")

@define_behavior
def py_bitor_sintX_strY(x: sint, y: str):
    raise TypeError("'|' not supported between instances of 'int' and 'str'")

@define_behavior
def py_bitor_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_bintX_floatY(x: bint, y: float):
    raise TypeError("'|' not supported between instances of 'int' and 'float'")

@define_behavior
def py_bitor_bintX_strY(x: bint, y: str):
    raise TypeError("'|' not supported between instances of 'int' and 'str'")

@define_behavior
def py_bitor_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_bitor_boolX_boolY(x: bool, y: bool):
    return True if x is True else y

@define_behavior
def py_bitor_boolX_floatY(x: bool, y: float):
    raise TypeError("'|' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_bitor_boolX_strY(x: bool, y: str):
    raise TypeError("'|' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_bitor_floatX_sintY(x: float, y: sint):
    raise TypeError("'|' not supported between instances of 'float' and 'int'")

@define_behavior
def py_bitor_floatX_bintY(x: float, y: bint):
    raise TypeError("'|' not supported between instances of 'float' and 'int'")

@define_behavior
def py_bitor_floatX_boolY(x: float, y: bool):
    raise TypeError("'|' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_bitor_floatX_floatY(x: float, y: float):
    raise TypeError("'|' not supported between instances of 'float' and 'float'")

@define_behavior
def py_bitor_floatX_strY(x: float, y: str):
    raise TypeError("'|' not supported between instances of 'float' and 'str'")

@define_behavior
def py_bitor_strX_sintY(x: str, y: sint):
    raise TypeError("'|' not supported between instances of 'str' and 'int'")

@define_behavior
def py_bitor_strX_bintY(x: str, y: bint):
    raise TypeError("'|' not supported between instances of 'str' and 'int'")

@define_behavior
def py_bitor_strX_boolY(x: str, y: bool):
    raise TypeError("'|' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_bitor_strX_floatY(x: str, y: float):
    raise TypeError("'|' not supported between instances of 'str' and 'float'")

@define_behavior
def py_bitor_strX_strY(x: str, y: str):
    raise TypeError("'|' not supported between instances of 'str' and 'str'")

@define_behavior
def py_floordiv_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_floordiv_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))

@define_behavior
def py_floordiv_sintX_boolY(x: sint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_floordiv_sintX_floatY(x: sint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_floordiv_sintX_strY(x: sint, y: str):
    raise TypeError("'//' not supported between instances of 'int' and 'str'")

@define_behavior
def py_floordiv_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_floordiv_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))

@define_behavior
def py_floordiv_bintX_boolY(x: bint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_floordiv_bintX_floatY(x: bint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_floordiv_bintX_strY(x: bint, y: str):
    raise TypeError("'//' not supported between instances of 'int' and 'str'")

@define_behavior
def py_floordiv_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_floordiv_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))

@define_behavior
def py_floordiv_boolX_boolY(x: bool, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_floordiv_boolX_floatY(x: bool, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_floordiv_boolX_strY(x: bool, y: str):
    raise TypeError("'//' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_floordiv_floatX_sintY(x: float, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_float_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_floordiv_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) // py_int_to_host(y))

@define_behavior
def py_floordiv_floatX_boolY(x: float, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_float_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_floordiv_floatX_floatY(x: float, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_float_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_floordiv_floatX_strY(x: float, y: str):
    raise TypeError("'//' not supported between instances of 'float' and 'str'")

@define_behavior
def py_floordiv_strX_sintY(x: str, y: sint):
    raise TypeError("'//' not supported between instances of 'str' and 'int'")

@define_behavior
def py_floordiv_strX_bintY(x: str, y: bint):
    raise TypeError("'//' not supported between instances of 'str' and 'int'")

@define_behavior
def py_floordiv_strX_boolY(x: str, y: bool):
    raise TypeError("'//' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_floordiv_strX_floatY(x: str, y: float):
    raise TypeError("'//' not supported between instances of 'str' and 'float'")

@define_behavior
def py_floordiv_strX_strY(x: str, y: str):
    raise TypeError("'//' not supported between instances of 'str' and 'str'")

@define_behavior
def py_lshift_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_sintX_bintY(x: sint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_sintX_boolY(x: sint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_sintX_floatY(x: sint, y: float):
    raise TypeError("'<<' not supported between instances of 'int' and 'float'")

@define_behavior
def py_lshift_sintX_strY(x: sint, y: str):
    raise TypeError("'<<' not supported between instances of 'int' and 'str'")

@define_behavior
def py_lshift_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_bintX_bintY(x: bint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_bintX_boolY(x: bint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_bintX_floatY(x: bint, y: float):
    raise TypeError("'<<' not supported between instances of 'int' and 'float'")

@define_behavior
def py_lshift_bintX_strY(x: bint, y: str):
    raise TypeError("'<<' not supported between instances of 'int' and 'str'")

@define_behavior
def py_lshift_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_boolX_bintY(x: bool, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_boolX_boolY(x: bool, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_lshift_boolX_floatY(x: bool, y: float):
    raise TypeError("'<<' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_lshift_boolX_strY(x: bool, y: str):
    raise TypeError("'<<' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_lshift_floatX_sintY(x: float, y: sint):
    raise TypeError("'<<' not supported between instances of 'float' and 'int'")

@define_behavior
def py_lshift_floatX_bintY(x: float, y: bint):
    raise TypeError("'<<' not supported between instances of 'float' and 'int'")

@define_behavior
def py_lshift_floatX_boolY(x: float, y: bool):
    raise TypeError("'<<' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_lshift_floatX_floatY(x: float, y: float):
    raise TypeError("'<<' not supported between instances of 'float' and 'float'")

@define_behavior
def py_lshift_floatX_strY(x: float, y: str):
    raise TypeError("'<<' not supported between instances of 'float' and 'str'")

@define_behavior
def py_lshift_strX_sintY(x: str, y: sint):
    raise TypeError("'<<' not supported between instances of 'str' and 'int'")

@define_behavior
def py_lshift_strX_bintY(x: str, y: bint):
    raise TypeError("'<<' not supported between instances of 'str' and 'int'")

@define_behavior
def py_lshift_strX_boolY(x: str, y: bool):
    raise TypeError("'<<' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_lshift_strX_floatY(x: str, y: float):
    raise TypeError("'<<' not supported between instances of 'str' and 'float'")

@define_behavior
def py_lshift_strX_strY(x: str, y: str):
    raise TypeError("'<<' not supported between instances of 'str' and 'str'")

@define_behavior
def py_matmul_sintX_sintY(x: sint, y: sint):
    raise TypeError("'@' not supported between instances of 'int' and 'int'")

@define_behavior
def py_matmul_sintX_bintY(x: sint, y: bint):
    raise TypeError("'@' not supported between instances of 'int' and 'int'")

@define_behavior
def py_matmul_sintX_boolY(x: sint, y: bool):
    raise TypeError("'@' not supported between instances of 'int' and 'bool'")

@define_behavior
def py_matmul_sintX_floatY(x: sint, y: float):
    raise TypeError("'@' not supported between instances of 'int' and 'float'")

@define_behavior
def py_matmul_sintX_strY(x: sint, y: str):
    raise TypeError("'@' not supported between instances of 'int' and 'str'")

@define_behavior
def py_matmul_bintX_sintY(x: bint, y: sint):
    raise TypeError("'@' not supported between instances of 'int' and 'int'")

@define_behavior
def py_matmul_bintX_bintY(x: bint, y: bint):
    raise TypeError("'@' not supported between instances of 'int' and 'int'")

@define_behavior
def py_matmul_bintX_boolY(x: bint, y: bool):
    raise TypeError("'@' not supported between instances of 'int' and 'bool'")

@define_behavior
def py_matmul_bintX_floatY(x: bint, y: float):
    raise TypeError("'@' not supported between instances of 'int' and 'float'")

@define_behavior
def py_matmul_bintX_strY(x: bint, y: str):
    raise TypeError("'@' not supported between instances of 'int' and 'str'")

@define_behavior
def py_matmul_boolX_sintY(x: bool, y: sint):
    raise TypeError("'@' not supported between instances of 'bool' and 'int'")

@define_behavior
def py_matmul_boolX_bintY(x: bool, y: bint):
    raise TypeError("'@' not supported between instances of 'bool' and 'int'")

@define_behavior
def py_matmul_boolX_boolY(x: bool, y: bool):
    raise TypeError("'@' not supported between instances of 'bool' and 'bool'")

@define_behavior
def py_matmul_boolX_floatY(x: bool, y: float):
    raise TypeError("'@' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_matmul_boolX_strY(x: bool, y: str):
    raise TypeError("'@' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_matmul_floatX_sintY(x: float, y: sint):
    raise TypeError("'@' not supported between instances of 'float' and 'int'")

@define_behavior
def py_matmul_floatX_bintY(x: float, y: bint):
    raise TypeError("'@' not supported between instances of 'float' and 'int'")

@define_behavior
def py_matmul_floatX_boolY(x: float, y: bool):
    raise TypeError("'@' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_matmul_floatX_floatY(x: float, y: float):
    raise TypeError("'@' not supported between instances of 'float' and 'float'")

@define_behavior
def py_matmul_floatX_strY(x: float, y: str):
    raise TypeError("'@' not supported between instances of 'float' and 'str'")

@define_behavior
def py_matmul_strX_sintY(x: str, y: sint):
    raise TypeError("'@' not supported between instances of 'str' and 'int'")

@define_behavior
def py_matmul_strX_bintY(x: str, y: bint):
    raise TypeError("'@' not supported between instances of 'str' and 'int'")

@define_behavior
def py_matmul_strX_boolY(x: str, y: bool):
    raise TypeError("'@' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_matmul_strX_floatY(x: str, y: float):
    raise TypeError("'@' not supported between instances of 'str' and 'float'")

@define_behavior
def py_matmul_strX_strY(x: str, y: str):
    raise TypeError("'@' not supported between instances of 'str' and 'str'")

@define_behavior
def py_mod_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_mod_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))

@define_behavior
def py_mod_sintX_boolY(x: sint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_mod_sintX_floatY(x: sint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_mod_sintX_strY(x: sint, y: str):
    raise TypeError("'%' not supported between instances of 'int' and 'str'")

@define_behavior
def py_mod_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_mod_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))

@define_behavior
def py_mod_bintX_boolY(x: bint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_mod_bintX_floatY(x: bint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_mod_bintX_strY(x: bint, y: str):
    raise TypeError("'%' not supported between instances of 'int' and 'str'")

@define_behavior
def py_mod_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_mod_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))

@define_behavior
def py_mod_boolX_boolY(x: bool, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_mod_boolX_floatY(x: bool, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_mod_boolX_strY(x: bool, y: str):
    raise TypeError("'%' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_mod_floatX_sintY(x: float, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_float_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_mod_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) % py_int_to_host(y))

@define_behavior
def py_mod_floatX_boolY(x: float, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_float_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_mod_floatX_floatY(x: float, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_float_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_mod_floatX_strY(x: float, y: str):
    raise TypeError("'%' not supported between instances of 'float' and 'str'")

@define_behavior
def py_mul_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) * py_float_to_host(y))

@define_behavior
def py_mul_sintX_strY(x: sint, y: str):
    return py_str_from_host(py_str_to_host(y) * py_int_to_host(x))

@define_behavior
def py_mul_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) * py_float_to_host(y))

@define_behavior
def py_mul_bintX_strY(x: bint, y: str):
    return py_str_from_host(py_str_to_host(y) * py_int_to_host(x))

@define_behavior
def py_mul_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) * py_float_to_host(y))

@define_behavior
def py_mul_boolX_strY(x: bool, y: str):
    return py_str_from_host(py_str_to_host(y) * py_int_to_host(x))

@define_behavior
def py_mul_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) * py_float_to_host(y))

@define_behavior
def py_mul_floatX_strY(x: float, y: str):
    raise TypeError("'*' not supported between instances of 'float' and 'str'")

@define_behavior
def py_mul_strX_sintY(x: str, y: sint):
    return py_str_from_host(py_str_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_strX_bintY(x: str, y: bint):
    return py_str_from_host(py_str_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_strX_boolY(x: str, y: bool):
    return py_str_from_host(py_str_to_host(x) * py_int_to_host(y))

@define_behavior
def py_mul_strX_floatY(x: str, y: float):
    raise TypeError("'*' not supported between instances of 'str' and 'float'")

@define_behavior
def py_mul_strX_strY(x: str, y: str):
    raise TypeError("'*' not supported between instances of 'str' and 'str'")

@define_behavior
def py_pow_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_pow_sintX_strY(x: sint, y: str):
    raise TypeError("'**' not supported between instances of 'int' and 'str'")

@define_behavior
def py_pow_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_pow_bintX_strY(x: bint, y: str):
    raise TypeError("'**' not supported between instances of 'int' and 'str'")

@define_behavior
def py_pow_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_pow_boolX_strY(x: bool, y: str):
    raise TypeError("'**' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_pow_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_pow_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_pow_floatX_strY(x: float, y: str):
    raise TypeError("'**' not supported between instances of 'float' and 'str'")

@define_behavior
def py_pow_strX_sintY(x: str, y: sint):
    raise TypeError("'**' not supported between instances of 'str' and 'int'")

@define_behavior
def py_pow_strX_bintY(x: str, y: bint):
    raise TypeError("'**' not supported between instances of 'str' and 'int'")

@define_behavior
def py_pow_strX_boolY(x: str, y: bool):
    raise TypeError("'**' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_pow_strX_floatY(x: str, y: float):
    raise TypeError("'**' not supported between instances of 'str' and 'float'")

@define_behavior
def py_pow_strX_strY(x: str, y: str):
    raise TypeError("'**' not supported between instances of 'str' and 'str'")

@define_behavior
def py_rshift_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_sintX_bintY(x: sint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_sintX_boolY(x: sint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_sintX_floatY(x: sint, y: float):
    raise TypeError("'>>' not supported between instances of 'int' and 'float'")

@define_behavior
def py_rshift_sintX_strY(x: sint, y: str):
    raise TypeError("'>>' not supported between instances of 'int' and 'str'")

@define_behavior
def py_rshift_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_bintX_bintY(x: bint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_bintX_boolY(x: bint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_bintX_floatY(x: bint, y: float):
    raise TypeError("'>>' not supported between instances of 'int' and 'float'")

@define_behavior
def py_rshift_bintX_strY(x: bint, y: str):
    raise TypeError("'>>' not supported between instances of 'int' and 'str'")

@define_behavior
def py_rshift_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_boolX_bintY(x: bool, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_boolX_boolY(x: bool, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_rshift_boolX_floatY(x: bool, y: float):
    raise TypeError("'>>' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_rshift_boolX_strY(x: bool, y: str):
    raise TypeError("'>>' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_rshift_floatX_sintY(x: float, y: sint):
    raise TypeError("'>>' not supported between instances of 'float' and 'int'")

@define_behavior
def py_rshift_floatX_bintY(x: float, y: bint):
    raise TypeError("'>>' not supported between instances of 'float' and 'int'")

@define_behavior
def py_rshift_floatX_boolY(x: float, y: bool):
    raise TypeError("'>>' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_rshift_floatX_floatY(x: float, y: float):
    raise TypeError("'>>' not supported between instances of 'float' and 'float'")

@define_behavior
def py_rshift_floatX_strY(x: float, y: str):
    raise TypeError("'>>' not supported between instances of 'float' and 'str'")

@define_behavior
def py_rshift_strX_sintY(x: str, y: sint):
    raise TypeError("'>>' not supported between instances of 'str' and 'int'")

@define_behavior
def py_rshift_strX_bintY(x: str, y: bint):
    raise TypeError("'>>' not supported between instances of 'str' and 'int'")

@define_behavior
def py_rshift_strX_boolY(x: str, y: bool):
    raise TypeError("'>>' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_rshift_strX_floatY(x: str, y: float):
    raise TypeError("'>>' not supported between instances of 'str' and 'float'")

@define_behavior
def py_rshift_strX_strY(x: str, y: str):
    raise TypeError("'>>' not supported between instances of 'str' and 'str'")

@define_behavior
def py_sub_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) - py_float_to_host(y))

@define_behavior
def py_sub_sintX_strY(x: sint, y: str):
    raise TypeError("'-' not supported between instances of 'int' and 'str'")

@define_behavior
def py_sub_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) - py_float_to_host(y))

@define_behavior
def py_sub_bintX_strY(x: bint, y: str):
    raise TypeError("'-' not supported between instances of 'int' and 'str'")

@define_behavior
def py_sub_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) - py_float_to_host(y))

@define_behavior
def py_sub_boolX_strY(x: bool, y: str):
    raise TypeError("'-' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_sub_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) - py_int_to_host(y))

@define_behavior
def py_sub_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) - py_float_to_host(y))

@define_behavior
def py_sub_floatX_strY(x: float, y: str):
    raise TypeError("'-' not supported between instances of 'float' and 'str'")

@define_behavior
def py_sub_strX_sintY(x: str, y: sint):
    raise TypeError("'-' not supported between instances of 'str' and 'int'")

@define_behavior
def py_sub_strX_bintY(x: str, y: bint):
    raise TypeError("'-' not supported between instances of 'str' and 'int'")

@define_behavior
def py_sub_strX_boolY(x: str, y: bool):
    raise TypeError("'-' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_sub_strX_floatY(x: str, y: float):
    raise TypeError("'-' not supported between instances of 'str' and 'float'")

@define_behavior
def py_sub_strX_strY(x: str, y: str):
    raise TypeError("'-' not supported between instances of 'str' and 'str'")

@define_behavior
def py_truediv_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_truediv_sintX_bintY(x: sint, y: bint):
    return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))

@define_behavior
def py_truediv_sintX_boolY(x: sint, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_truediv_sintX_floatY(x: sint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_truediv_sintX_strY(x: sint, y: str):
    raise TypeError("'/' not supported between instances of 'int' and 'str'")

@define_behavior
def py_truediv_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_truediv_bintX_bintY(x: bint, y: bint):
    return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))

@define_behavior
def py_truediv_bintX_boolY(x: bint, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_truediv_bintX_floatY(x: bint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_truediv_bintX_strY(x: bint, y: str):
    raise TypeError("'/' not supported between instances of 'int' and 'str'")

@define_behavior
def py_truediv_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_truediv_boolX_bintY(x: bool, y: bint):
    return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))

@define_behavior
def py_truediv_boolX_boolY(x: bool, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_truediv_boolX_floatY(x: bool, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_truediv_boolX_strY(x: bool, y: str):
    raise TypeError("'/' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_truediv_floatX_sintY(x: float, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_float_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_truediv_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) / py_int_to_host(y))

@define_behavior
def py_truediv_floatX_boolY(x: float, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_float_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_truediv_floatX_floatY(x: float, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_float_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_truediv_floatX_strY(x: float, y: str):
    raise TypeError("'/' not supported between instances of 'float' and 'str'")

@define_behavior
def py_truediv_strX_sintY(x: str, y: sint):
    raise TypeError("'/' not supported between instances of 'str' and 'int'")

@define_behavior
def py_truediv_strX_bintY(x: str, y: bint):
    raise TypeError("'/' not supported between instances of 'str' and 'int'")

@define_behavior
def py_truediv_strX_boolY(x: str, y: bool):
    raise TypeError("'/' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_truediv_strX_floatY(x: str, y: float):
    raise TypeError("'/' not supported between instances of 'str' and 'float'")

@define_behavior
def py_truediv_strX_strY(x: str, y: str):
    raise TypeError("'/' not supported between instances of 'str' and 'str'")

@define_behavior
def py_xor_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_sintX_floatY(x: sint, y: float):
    raise TypeError("'^' not supported between instances of 'int' and 'float'")

@define_behavior
def py_xor_sintX_strY(x: sint, y: str):
    raise TypeError("'^' not supported between instances of 'int' and 'str'")

@define_behavior
def py_xor_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_bintX_floatY(x: bint, y: float):
    raise TypeError("'^' not supported between instances of 'int' and 'float'")

@define_behavior
def py_xor_bintX_strY(x: bint, y: str):
    raise TypeError("'^' not supported between instances of 'int' and 'str'")

@define_behavior
def py_xor_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_xor_boolX_boolY(x: bool, y: bool):
    return x is not y

@define_behavior
def py_xor_boolX_floatY(x: bool, y: float):
    raise TypeError("'^' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_xor_boolX_strY(x: bool, y: str):
    raise TypeError("'^' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_xor_floatX_sintY(x: float, y: sint):
    raise TypeError("'^' not supported between instances of 'float' and 'int'")

@define_behavior
def py_xor_floatX_bintY(x: float, y: bint):
    raise TypeError("'^' not supported between instances of 'float' and 'int'")

@define_behavior
def py_xor_floatX_boolY(x: float, y: bool):
    raise TypeError("'^' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_xor_floatX_floatY(x: float, y: float):
    raise TypeError("'^' not supported between instances of 'float' and 'float'")

@define_behavior
def py_xor_floatX_strY(x: float, y: str):
    raise TypeError("'^' not supported between instances of 'float' and 'str'")

@define_behavior
def py_xor_strX_sintY(x: str, y: sint):
    raise TypeError("'^' not supported between instances of 'str' and 'int'")

@define_behavior
def py_xor_strX_bintY(x: str, y: bint):
    raise TypeError("'^' not supported between instances of 'str' and 'int'")

@define_behavior
def py_xor_strX_boolY(x: str, y: bool):
    raise TypeError("'^' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_xor_strX_floatY(x: str, y: float):
    raise TypeError("'^' not supported between instances of 'str' and 'float'")

@define_behavior
def py_xor_strX_strY(x: str, y: str):
    raise TypeError("'^' not supported between instances of 'str' and 'str'")

@define_behavior
def py_iadd_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) + py_float_to_host(y))

@define_behavior
def py_iadd_sintX_strY(x: sint, y: str):
    raise TypeError("'+=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_iadd_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) + py_float_to_host(y))

@define_behavior
def py_iadd_bintX_strY(x: bint, y: str):
    raise TypeError("'+=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_iadd_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) + py_float_to_host(y))

@define_behavior
def py_iadd_boolX_strY(x: bool, y: str):
    raise TypeError("'+=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_iadd_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) + py_int_to_host(y))

@define_behavior
def py_iadd_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) + py_float_to_host(y))

@define_behavior
def py_iadd_floatX_strY(x: float, y: str):
    raise TypeError("'+=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_iadd_strX_sintY(x: str, y: sint):
    raise TypeError("'+=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_iadd_strX_bintY(x: str, y: bint):
    raise TypeError("'+=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_iadd_strX_boolY(x: str, y: bool):
    raise TypeError("'+=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_iadd_strX_floatY(x: str, y: float):
    raise TypeError("'+=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_iadd_strX_strY(x: str, y: str):
    return py_str_from_host(py_str_to_host(x) + py_str_to_host(y))

@define_behavior
def py_ibitand_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_sintX_floatY(x: sint, y: float):
    raise TypeError("'&=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ibitand_sintX_strY(x: sint, y: str):
    raise TypeError("'&=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ibitand_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_bintX_floatY(x: bint, y: float):
    raise TypeError("'&=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ibitand_bintX_strY(x: bint, y: str):
    raise TypeError("'&=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ibitand_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) & py_int_to_host(y))

@define_behavior
def py_ibitand_boolX_floatY(x: bool, y: float):
    raise TypeError("'&=' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_ibitand_boolX_strY(x: bool, y: str):
    raise TypeError("'&=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ibitand_floatX_sintY(x: float, y: sint):
    raise TypeError("'&=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ibitand_floatX_bintY(x: float, y: bint):
    raise TypeError("'&=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ibitand_floatX_boolY(x: float, y: bool):
    raise TypeError("'&=' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_ibitand_floatX_floatY(x: float, y: float):
    raise TypeError("'&=' not supported between instances of 'float' and 'float'")

@define_behavior
def py_ibitand_floatX_strY(x: float, y: str):
    raise TypeError("'&=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ibitand_strX_sintY(x: str, y: sint):
    raise TypeError("'&=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ibitand_strX_bintY(x: str, y: bint):
    raise TypeError("'&=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ibitand_strX_boolY(x: str, y: bool):
    raise TypeError("'&=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ibitand_strX_floatY(x: str, y: float):
    raise TypeError("'&=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ibitand_strX_strY(x: str, y: str):
    raise TypeError("'&=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_ibitor_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_sintX_floatY(x: sint, y: float):
    raise TypeError("'|=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ibitor_sintX_strY(x: sint, y: str):
    raise TypeError("'|=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ibitor_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_bintX_floatY(x: bint, y: float):
    raise TypeError("'|=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ibitor_bintX_strY(x: bint, y: str):
    raise TypeError("'|=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ibitor_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) | py_int_to_host(y))

@define_behavior
def py_ibitor_boolX_floatY(x: bool, y: float):
    raise TypeError("'|=' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_ibitor_boolX_strY(x: bool, y: str):
    raise TypeError("'|=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ibitor_floatX_sintY(x: float, y: sint):
    raise TypeError("'|=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ibitor_floatX_bintY(x: float, y: bint):
    raise TypeError("'|=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ibitor_floatX_boolY(x: float, y: bool):
    raise TypeError("'|=' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_ibitor_floatX_floatY(x: float, y: float):
    raise TypeError("'|=' not supported between instances of 'float' and 'float'")

@define_behavior
def py_ibitor_floatX_strY(x: float, y: str):
    raise TypeError("'|=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ibitor_strX_sintY(x: str, y: sint):
    raise TypeError("'|=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ibitor_strX_bintY(x: str, y: bint):
    raise TypeError("'|=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ibitor_strX_boolY(x: str, y: bool):
    raise TypeError("'|=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ibitor_strX_floatY(x: str, y: float):
    raise TypeError("'|=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ibitor_strX_strY(x: str, y: str):
    raise TypeError("'|=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_ifloordiv_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_ifloordiv_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))

@define_behavior
def py_ifloordiv_sintX_boolY(x: sint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_ifloordiv_sintX_floatY(x: sint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_ifloordiv_sintX_strY(x: sint, y: str):
    raise TypeError("'//=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ifloordiv_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_ifloordiv_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))

@define_behavior
def py_ifloordiv_bintX_boolY(x: bint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_ifloordiv_bintX_floatY(x: bint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_ifloordiv_bintX_strY(x: bint, y: str):
    raise TypeError("'//=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ifloordiv_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_ifloordiv_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))

@define_behavior
def py_ifloordiv_boolX_boolY(x: bool, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('integer division by zero')

@define_behavior
def py_ifloordiv_boolX_floatY(x: bool, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_ifloordiv_boolX_strY(x: bool, y: str):
    raise TypeError("'//=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ifloordiv_floatX_sintY(x: float, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_float_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_ifloordiv_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) // py_int_to_host(y))

@define_behavior
def py_ifloordiv_floatX_boolY(x: float, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_float_to_host(x) // py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_ifloordiv_floatX_floatY(x: float, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_float_to_host(x) // py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_ifloordiv_floatX_strY(x: float, y: str):
    raise TypeError("'//=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ifloordiv_strX_sintY(x: str, y: sint):
    raise TypeError("'//=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ifloordiv_strX_bintY(x: str, y: bint):
    raise TypeError("'//=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ifloordiv_strX_boolY(x: str, y: bool):
    raise TypeError("'//=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ifloordiv_strX_floatY(x: str, y: float):
    raise TypeError("'//=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ifloordiv_strX_strY(x: str, y: str):
    raise TypeError("'//=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_ilshift_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_sintX_bintY(x: sint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_sintX_boolY(x: sint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_sintX_floatY(x: sint, y: float):
    raise TypeError("'<<=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ilshift_sintX_strY(x: sint, y: str):
    raise TypeError("'<<=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ilshift_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_bintX_bintY(x: bint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_bintX_boolY(x: bint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_bintX_floatY(x: bint, y: float):
    raise TypeError("'<<=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ilshift_bintX_strY(x: bint, y: str):
    raise TypeError("'<<=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ilshift_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_boolX_bintY(x: bool, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_boolX_boolY(x: bool, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) << py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_ilshift_boolX_floatY(x: bool, y: float):
    raise TypeError("'<<=' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_ilshift_boolX_strY(x: bool, y: str):
    raise TypeError("'<<=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ilshift_floatX_sintY(x: float, y: sint):
    raise TypeError("'<<=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ilshift_floatX_bintY(x: float, y: bint):
    raise TypeError("'<<=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ilshift_floatX_boolY(x: float, y: bool):
    raise TypeError("'<<=' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_ilshift_floatX_floatY(x: float, y: float):
    raise TypeError("'<<=' not supported between instances of 'float' and 'float'")

@define_behavior
def py_ilshift_floatX_strY(x: float, y: str):
    raise TypeError("'<<=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ilshift_strX_sintY(x: str, y: sint):
    raise TypeError("'<<=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ilshift_strX_bintY(x: str, y: bint):
    raise TypeError("'<<=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ilshift_strX_boolY(x: str, y: bool):
    raise TypeError("'<<=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ilshift_strX_floatY(x: str, y: float):
    raise TypeError("'<<=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ilshift_strX_strY(x: str, y: str):
    raise TypeError("'<<=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_imatmul_sintX_sintY(x: sint, y: sint):
    raise TypeError("'@=' not supported between instances of 'int' and 'int'")

@define_behavior
def py_imatmul_sintX_bintY(x: sint, y: bint):
    raise TypeError("'@=' not supported between instances of 'int' and 'int'")

@define_behavior
def py_imatmul_sintX_boolY(x: sint, y: bool):
    raise TypeError("'@=' not supported between instances of 'int' and 'bool'")

@define_behavior
def py_imatmul_sintX_floatY(x: sint, y: float):
    raise TypeError("'@=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_imatmul_sintX_strY(x: sint, y: str):
    raise TypeError("'@=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_imatmul_bintX_sintY(x: bint, y: sint):
    raise TypeError("'@=' not supported between instances of 'int' and 'int'")

@define_behavior
def py_imatmul_bintX_bintY(x: bint, y: bint):
    raise TypeError("'@=' not supported between instances of 'int' and 'int'")

@define_behavior
def py_imatmul_bintX_boolY(x: bint, y: bool):
    raise TypeError("'@=' not supported between instances of 'int' and 'bool'")

@define_behavior
def py_imatmul_bintX_floatY(x: bint, y: float):
    raise TypeError("'@=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_imatmul_bintX_strY(x: bint, y: str):
    raise TypeError("'@=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_imatmul_boolX_sintY(x: bool, y: sint):
    raise TypeError("'@=' not supported between instances of 'bool' and 'int'")

@define_behavior
def py_imatmul_boolX_bintY(x: bool, y: bint):
    raise TypeError("'@=' not supported between instances of 'bool' and 'int'")

@define_behavior
def py_imatmul_boolX_boolY(x: bool, y: bool):
    raise TypeError("'@=' not supported between instances of 'bool' and 'bool'")

@define_behavior
def py_imatmul_boolX_floatY(x: bool, y: float):
    raise TypeError("'@=' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_imatmul_boolX_strY(x: bool, y: str):
    raise TypeError("'@=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_imatmul_floatX_sintY(x: float, y: sint):
    raise TypeError("'@=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_imatmul_floatX_bintY(x: float, y: bint):
    raise TypeError("'@=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_imatmul_floatX_boolY(x: float, y: bool):
    raise TypeError("'@=' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_imatmul_floatX_floatY(x: float, y: float):
    raise TypeError("'@=' not supported between instances of 'float' and 'float'")

@define_behavior
def py_imatmul_floatX_strY(x: float, y: str):
    raise TypeError("'@=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_imatmul_strX_sintY(x: str, y: sint):
    raise TypeError("'@=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_imatmul_strX_bintY(x: str, y: bint):
    raise TypeError("'@=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_imatmul_strX_boolY(x: str, y: bool):
    raise TypeError("'@=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_imatmul_strX_floatY(x: str, y: float):
    raise TypeError("'@=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_imatmul_strX_strY(x: str, y: str):
    raise TypeError("'@=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_imod_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_imod_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))

@define_behavior
def py_imod_sintX_boolY(x: sint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_imod_sintX_floatY(x: sint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_imod_sintX_strY(x: sint, y: str):
    raise TypeError("'%=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_imod_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_imod_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))

@define_behavior
def py_imod_bintX_boolY(x: bint, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_imod_bintX_floatY(x: bint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_imod_bintX_strY(x: bint, y: str):
    raise TypeError("'%=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_imod_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_imod_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))

@define_behavior
def py_imod_boolX_boolY(x: bool, y: bool):
    if py_bool_to_host_bool(y):
        return py_int_from_host(py_int_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('modulo by zero')

@define_behavior
def py_imod_boolX_floatY(x: bool, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_imod_boolX_strY(x: bool, y: str):
    raise TypeError("'%=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_imod_floatX_sintY(x: float, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_float_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_imod_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) % py_int_to_host(y))

@define_behavior
def py_imod_floatX_boolY(x: float, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_float_to_host(x) % py_int_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_imod_floatX_floatY(x: float, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_float_to_host(x) % py_float_to_host(y))
    else:
        raise ZeroDivisionError('float modulo by zero')

@define_behavior
def py_imod_floatX_strY(x: float, y: str):
    raise TypeError("'%=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_imul_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) * py_float_to_host(y))

@define_behavior
def py_imul_sintX_strY(x: sint, y: str):
    return py_str_from_host(py_str_to_host(y) * py_int_to_host(x))

@define_behavior
def py_imul_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) * py_float_to_host(y))

@define_behavior
def py_imul_bintX_strY(x: bint, y: str):
    return py_str_from_host(py_str_to_host(y) * py_int_to_host(x))

@define_behavior
def py_imul_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) * py_float_to_host(y))

@define_behavior
def py_imul_boolX_strY(x: bool, y: str):
    return py_str_from_host(py_str_to_host(y) * py_int_to_host(x))

@define_behavior
def py_imul_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) * py_float_to_host(y))

@define_behavior
def py_imul_floatX_strY(x: float, y: str):
    raise TypeError("'*=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_imul_strX_sintY(x: str, y: sint):
    return py_str_from_host(py_str_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_strX_bintY(x: str, y: bint):
    return py_str_from_host(py_str_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_strX_boolY(x: str, y: bool):
    return py_str_from_host(py_str_to_host(x) * py_int_to_host(y))

@define_behavior
def py_imul_strX_floatY(x: str, y: float):
    raise TypeError("'*=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_imul_strX_strY(x: str, y: str):
    raise TypeError("'*=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_ipow_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_ipow_sintX_strY(x: sint, y: str):
    raise TypeError("'**=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ipow_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_ipow_bintX_strY(x: bint, y: str):
    raise TypeError("'**=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ipow_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_ipow_boolX_strY(x: bool, y: str):
    raise TypeError("'**=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ipow_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) ** py_int_to_host(y))

@define_behavior
def py_ipow_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) ** py_float_to_host(y))

@define_behavior
def py_ipow_floatX_strY(x: float, y: str):
    raise TypeError("'**=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ipow_strX_sintY(x: str, y: sint):
    raise TypeError("'**=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ipow_strX_bintY(x: str, y: bint):
    raise TypeError("'**=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ipow_strX_boolY(x: str, y: bool):
    raise TypeError("'**=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ipow_strX_floatY(x: str, y: float):
    raise TypeError("'**=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ipow_strX_strY(x: str, y: str):
    raise TypeError("'**=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_irshift_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_sintX_bintY(x: sint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_sintX_boolY(x: sint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_sintX_floatY(x: sint, y: float):
    raise TypeError("'>>=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_irshift_sintX_strY(x: sint, y: str):
    raise TypeError("'>>=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_irshift_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_bintX_bintY(x: bint, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_bintX_boolY(x: bint, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_bintX_floatY(x: bint, y: float):
    raise TypeError("'>>=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_irshift_bintX_strY(x: bint, y: str):
    raise TypeError("'>>=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_irshift_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_boolX_bintY(x: bool, y: bint):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_boolX_boolY(x: bool, y: bool):
    if py_int_to_host(y) >= py_int_to_host(0):
        return py_int_from_host(py_int_to_host(x) >> py_int_to_host(y))
    else:
        raise ValueError('negative shift count')

@define_behavior
def py_irshift_boolX_floatY(x: bool, y: float):
    raise TypeError("'>>=' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_irshift_boolX_strY(x: bool, y: str):
    raise TypeError("'>>=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_irshift_floatX_sintY(x: float, y: sint):
    raise TypeError("'>>=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_irshift_floatX_bintY(x: float, y: bint):
    raise TypeError("'>>=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_irshift_floatX_boolY(x: float, y: bool):
    raise TypeError("'>>=' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_irshift_floatX_floatY(x: float, y: float):
    raise TypeError("'>>=' not supported between instances of 'float' and 'float'")

@define_behavior
def py_irshift_floatX_strY(x: float, y: str):
    raise TypeError("'>>=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_irshift_strX_sintY(x: str, y: sint):
    raise TypeError("'>>=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_irshift_strX_bintY(x: str, y: bint):
    raise TypeError("'>>=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_irshift_strX_boolY(x: str, y: bool):
    raise TypeError("'>>=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_irshift_strX_floatY(x: str, y: float):
    raise TypeError("'>>=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_irshift_strX_strY(x: str, y: str):
    raise TypeError("'>>=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_isub_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_sintX_floatY(x: sint, y: float):
    return py_float_from_host(py_int_to_host(x) - py_float_to_host(y))

@define_behavior
def py_isub_sintX_strY(x: sint, y: str):
    raise TypeError("'-=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_isub_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_bintX_floatY(x: bint, y: float):
    return py_float_from_host(py_int_to_host(x) - py_float_to_host(y))

@define_behavior
def py_isub_bintX_strY(x: bint, y: str):
    raise TypeError("'-=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_isub_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_boolX_floatY(x: bool, y: float):
    return py_float_from_host(py_int_to_host(x) - py_float_to_host(y))

@define_behavior
def py_isub_boolX_strY(x: bool, y: str):
    raise TypeError("'-=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_isub_floatX_sintY(x: float, y: sint):
    return py_float_from_host(py_float_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_floatX_boolY(x: float, y: bool):
    return py_float_from_host(py_float_to_host(x) - py_int_to_host(y))

@define_behavior
def py_isub_floatX_floatY(x: float, y: float):
    return py_float_from_host(py_float_to_host(x) - py_float_to_host(y))

@define_behavior
def py_isub_floatX_strY(x: float, y: str):
    raise TypeError("'-=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_isub_strX_sintY(x: str, y: sint):
    raise TypeError("'-=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_isub_strX_bintY(x: str, y: bint):
    raise TypeError("'-=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_isub_strX_boolY(x: str, y: bool):
    raise TypeError("'-=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_isub_strX_floatY(x: str, y: float):
    raise TypeError("'-=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_isub_strX_strY(x: str, y: str):
    raise TypeError("'-=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_itruediv_sintX_sintY(x: sint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_itruediv_sintX_bintY(x: sint, y: bint):
    return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))

@define_behavior
def py_itruediv_sintX_boolY(x: sint, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_itruediv_sintX_floatY(x: sint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_itruediv_sintX_strY(x: sint, y: str):
    raise TypeError("'/=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_itruediv_bintX_sintY(x: bint, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_itruediv_bintX_bintY(x: bint, y: bint):
    return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))

@define_behavior
def py_itruediv_bintX_boolY(x: bint, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_itruediv_bintX_floatY(x: bint, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_itruediv_bintX_strY(x: bint, y: str):
    raise TypeError("'/=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_itruediv_boolX_sintY(x: bool, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_itruediv_boolX_bintY(x: bool, y: bint):
    return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))

@define_behavior
def py_itruediv_boolX_boolY(x: bool, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_int_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('division by zero')

@define_behavior
def py_itruediv_boolX_floatY(x: bool, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_int_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_itruediv_boolX_strY(x: bool, y: str):
    raise TypeError("'/=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_itruediv_floatX_sintY(x: float, y: sint):
    if py_int_to_host(y) != py_int_to_host(0):
        return py_float_from_host(py_float_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_itruediv_floatX_bintY(x: float, y: bint):
    return py_float_from_host(py_float_to_host(x) / py_int_to_host(y))

@define_behavior
def py_itruediv_floatX_boolY(x: float, y: bool):
    if py_bool_to_host_bool(y):
        return py_float_from_host(py_float_to_host(x) / py_int_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_itruediv_floatX_floatY(x: float, y: float):
    if py_float_to_host(y) != py_float_to_host(0.0):
        return py_float_from_host(py_float_to_host(x) / py_float_to_host(y))
    else:
        raise ZeroDivisionError('float division by zero')

@define_behavior
def py_itruediv_floatX_strY(x: float, y: str):
    raise TypeError("'/=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_itruediv_strX_sintY(x: str, y: sint):
    raise TypeError("'/=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_itruediv_strX_bintY(x: str, y: bint):
    raise TypeError("'/=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_itruediv_strX_boolY(x: str, y: bool):
    raise TypeError("'/=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_itruediv_strX_floatY(x: str, y: float):
    raise TypeError("'/=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_itruediv_strX_strY(x: str, y: str):
    raise TypeError("'/=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_ixor_sintX_sintY(x: sint, y: sint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_sintX_bintY(x: sint, y: bint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_sintX_boolY(x: sint, y: bool):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_sintX_floatY(x: sint, y: float):
    raise TypeError("'^=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ixor_sintX_strY(x: sint, y: str):
    raise TypeError("'^=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ixor_bintX_sintY(x: bint, y: sint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_bintX_bintY(x: bint, y: bint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_bintX_boolY(x: bint, y: bool):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_bintX_floatY(x: bint, y: float):
    raise TypeError("'^=' not supported between instances of 'int' and 'float'")

@define_behavior
def py_ixor_bintX_strY(x: bint, y: str):
    raise TypeError("'^=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ixor_boolX_sintY(x: bool, y: sint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_boolX_bintY(x: bool, y: bint):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_boolX_boolY(x: bool, y: bool):
    return py_int_from_host(py_int_to_host(x) ^ py_int_to_host(y))

@define_behavior
def py_ixor_boolX_floatY(x: bool, y: float):
    raise TypeError("'^=' not supported between instances of 'bool' and 'float'")

@define_behavior
def py_ixor_boolX_strY(x: bool, y: str):
    raise TypeError("'^=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ixor_floatX_sintY(x: float, y: sint):
    raise TypeError("'^=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ixor_floatX_bintY(x: float, y: bint):
    raise TypeError("'^=' not supported between instances of 'float' and 'int'")

@define_behavior
def py_ixor_floatX_boolY(x: float, y: bool):
    raise TypeError("'^=' not supported between instances of 'float' and 'bool'")

@define_behavior
def py_ixor_floatX_floatY(x: float, y: float):
    raise TypeError("'^=' not supported between instances of 'float' and 'float'")

@define_behavior
def py_ixor_floatX_strY(x: float, y: str):
    raise TypeError("'^=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ixor_strX_sintY(x: str, y: sint):
    raise TypeError("'^=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ixor_strX_bintY(x: str, y: bint):
    raise TypeError("'^=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ixor_strX_boolY(x: str, y: bool):
    raise TypeError("'^=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ixor_strX_floatY(x: str, y: float):
    raise TypeError("'^=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ixor_strX_strY(x: str, y: str):
    raise TypeError("'^=' not supported between instances of 'str' and 'str'")

@define_behavior
def py_ge_sintX_sintY(x: sint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_sintX_bintY(x: sint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_sintX_boolY(x: sint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_sintX_floatY(x: sint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) <= py_int_to_host(x))

@define_behavior
def py_ge_sintX_strY(x: sint, y: str):
    raise TypeError("'>=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ge_bintX_sintY(x: bint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_bintX_bintY(x: bint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_bintX_boolY(x: bint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_bintX_floatY(x: bint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) <= py_int_to_host(x))

@define_behavior
def py_ge_bintX_strY(x: bint, y: str):
    raise TypeError("'>=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_ge_boolX_sintY(x: bool, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_boolX_bintY(x: bool, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_boolX_boolY(x: bool, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_boolX_floatY(x: bool, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) <= py_int_to_host(x))

@define_behavior
def py_ge_boolX_strY(x: bool, y: str):
    raise TypeError("'>=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_ge_floatX_sintY(x: float, y: sint):
    return py_bool_from_host_bool(py_float_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_floatX_bintY(x: float, y: bint):
    return py_bool_from_host_bool(py_float_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_floatX_boolY(x: float, y: bool):
    return py_bool_from_host_bool(py_float_to_host(x) >= py_int_to_host(y))

@define_behavior
def py_ge_floatX_floatY(x: float, y: float):
    return py_bool_from_host_bool(py_float_to_host(x) >= py_float_to_host(y))

@define_behavior
def py_ge_floatX_strY(x: float, y: str):
    raise TypeError("'>=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_ge_strX_sintY(x: str, y: sint):
    raise TypeError("'>=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ge_strX_bintY(x: str, y: bint):
    raise TypeError("'>=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_ge_strX_boolY(x: str, y: bool):
    raise TypeError("'>=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_ge_strX_floatY(x: str, y: float):
    raise TypeError("'>=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_ge_strX_strY(x: str, y: str):
    return py_bool_from_host_bool(py_str_to_host(x) >= py_str_to_host(y))

@define_behavior
def py_gt_sintX_sintY(x: sint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_sintX_bintY(x: sint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_sintX_boolY(x: sint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_sintX_floatY(x: sint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) < py_int_to_host(x))

@define_behavior
def py_gt_sintX_strY(x: sint, y: str):
    raise TypeError("'>' not supported between instances of 'int' and 'str'")

@define_behavior
def py_gt_bintX_sintY(x: bint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_bintX_bintY(x: bint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_bintX_boolY(x: bint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_bintX_floatY(x: bint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) < py_int_to_host(x))

@define_behavior
def py_gt_bintX_strY(x: bint, y: str):
    raise TypeError("'>' not supported between instances of 'int' and 'str'")

@define_behavior
def py_gt_boolX_sintY(x: bool, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_boolX_bintY(x: bool, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_boolX_boolY(x: bool, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_boolX_floatY(x: bool, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) < py_int_to_host(x))

@define_behavior
def py_gt_boolX_strY(x: bool, y: str):
    raise TypeError("'>' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_gt_floatX_sintY(x: float, y: sint):
    return py_bool_from_host_bool(py_float_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_floatX_bintY(x: float, y: bint):
    return py_bool_from_host_bool(py_float_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_floatX_boolY(x: float, y: bool):
    return py_bool_from_host_bool(py_float_to_host(x) > py_int_to_host(y))

@define_behavior
def py_gt_floatX_floatY(x: float, y: float):
    return py_bool_from_host_bool(py_float_to_host(x) > py_float_to_host(y))

@define_behavior
def py_gt_floatX_strY(x: float, y: str):
    raise TypeError("'>' not supported between instances of 'float' and 'str'")

@define_behavior
def py_gt_strX_sintY(x: str, y: sint):
    raise TypeError("'>' not supported between instances of 'str' and 'int'")

@define_behavior
def py_gt_strX_bintY(x: str, y: bint):
    raise TypeError("'>' not supported between instances of 'str' and 'int'")

@define_behavior
def py_gt_strX_boolY(x: str, y: bool):
    raise TypeError("'>' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_gt_strX_floatY(x: str, y: float):
    raise TypeError("'>' not supported between instances of 'str' and 'float'")

@define_behavior
def py_gt_strX_strY(x: str, y: str):
    return py_bool_from_host_bool(py_str_to_host(x) > py_str_to_host(y))

@define_behavior
def py_le_sintX_sintY(x: sint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_sintX_bintY(x: sint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_sintX_boolY(x: sint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_sintX_floatY(x: sint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) >= py_int_to_host(x))

@define_behavior
def py_le_sintX_strY(x: sint, y: str):
    raise TypeError("'<=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_le_bintX_sintY(x: bint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_bintX_bintY(x: bint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_bintX_boolY(x: bint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_bintX_floatY(x: bint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) >= py_int_to_host(x))

@define_behavior
def py_le_bintX_strY(x: bint, y: str):
    raise TypeError("'<=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_le_boolX_sintY(x: bool, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_boolX_bintY(x: bool, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_boolX_boolY(x: bool, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_boolX_floatY(x: bool, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) >= py_int_to_host(x))

@define_behavior
def py_le_boolX_strY(x: bool, y: str):
    raise TypeError("'<=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_le_floatX_sintY(x: float, y: sint):
    return py_bool_from_host_bool(py_float_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_floatX_bintY(x: float, y: bint):
    return py_bool_from_host_bool(py_float_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_floatX_boolY(x: float, y: bool):
    return py_bool_from_host_bool(py_float_to_host(x) <= py_int_to_host(y))

@define_behavior
def py_le_floatX_floatY(x: float, y: float):
    return py_bool_from_host_bool(py_float_to_host(x) <= py_float_to_host(y))

@define_behavior
def py_le_floatX_strY(x: float, y: str):
    raise TypeError("'<=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_le_strX_sintY(x: str, y: sint):
    raise TypeError("'<=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_le_strX_bintY(x: str, y: bint):
    raise TypeError("'<=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_le_strX_boolY(x: str, y: bool):
    raise TypeError("'<=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_le_strX_floatY(x: str, y: float):
    raise TypeError("'<=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_le_strX_strY(x: str, y: str):
    return py_bool_from_host_bool(py_str_to_host(x) <= py_str_to_host(y))

@define_behavior
def py_lt_sintX_sintY(x: sint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_sintX_bintY(x: sint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_sintX_boolY(x: sint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_sintX_floatY(x: sint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) > py_int_to_host(x))

@define_behavior
def py_lt_sintX_strY(x: sint, y: str):
    raise TypeError("'<' not supported between instances of 'int' and 'str'")

@define_behavior
def py_lt_bintX_sintY(x: bint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_bintX_bintY(x: bint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_bintX_boolY(x: bint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_bintX_floatY(x: bint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) > py_int_to_host(x))

@define_behavior
def py_lt_bintX_strY(x: bint, y: str):
    raise TypeError("'<' not supported between instances of 'int' and 'str'")

@define_behavior
def py_lt_boolX_sintY(x: bool, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_boolX_bintY(x: bool, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_boolX_boolY(x: bool, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_boolX_floatY(x: bool, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) > py_int_to_host(x))

@define_behavior
def py_lt_boolX_strY(x: bool, y: str):
    raise TypeError("'<' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_lt_floatX_sintY(x: float, y: sint):
    return py_bool_from_host_bool(py_float_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_floatX_bintY(x: float, y: bint):
    return py_bool_from_host_bool(py_float_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_floatX_boolY(x: float, y: bool):
    return py_bool_from_host_bool(py_float_to_host(x) < py_int_to_host(y))

@define_behavior
def py_lt_floatX_floatY(x: float, y: float):
    return py_bool_from_host_bool(py_float_to_host(x) < py_float_to_host(y))

@define_behavior
def py_lt_floatX_strY(x: float, y: str):
    raise TypeError("'<' not supported between instances of 'float' and 'str'")

@define_behavior
def py_lt_strX_sintY(x: str, y: sint):
    raise TypeError("'<' not supported between instances of 'str' and 'int'")

@define_behavior
def py_lt_strX_bintY(x: str, y: bint):
    raise TypeError("'<' not supported between instances of 'str' and 'int'")

@define_behavior
def py_lt_strX_boolY(x: str, y: bool):
    raise TypeError("'<' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_lt_strX_floatY(x: str, y: float):
    raise TypeError("'<' not supported between instances of 'str' and 'float'")

@define_behavior
def py_lt_strX_strY(x: str, y: str):
    return py_bool_from_host_bool(py_str_to_host(x) < py_str_to_host(y))

@define_behavior
def py_eq_sintX_sintY(x: sint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_sintX_bintY(x: sint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_sintX_boolY(x: sint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_sintX_floatY(x: sint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) == py_int_to_host(x))

@define_behavior
def py_eq_sintX_strY(x: sint, y: str):
    return False

@define_behavior
def py_eq_bintX_sintY(x: bint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_bintX_bintY(x: bint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_bintX_boolY(x: bint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_bintX_floatY(x: bint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) == py_int_to_host(x))

@define_behavior
def py_eq_bintX_strY(x: bint, y: str):
    return False

@define_behavior
def py_eq_boolX_sintY(x: bool, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_boolX_bintY(x: bool, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_boolX_boolY(x: bool, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_boolX_floatY(x: bool, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) == py_int_to_host(x))

@define_behavior
def py_eq_boolX_strY(x: bool, y: str):
    return False

@define_behavior
def py_eq_floatX_sintY(x: float, y: sint):
    return py_bool_from_host_bool(py_float_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_floatX_bintY(x: float, y: bint):
    return py_bool_from_host_bool(py_float_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_floatX_boolY(x: float, y: bool):
    return py_bool_from_host_bool(py_float_to_host(x) == py_int_to_host(y))

@define_behavior
def py_eq_floatX_floatY(x: float, y: float):
    return py_bool_from_host_bool(py_float_to_host(x) == py_float_to_host(y))

@define_behavior
def py_eq_floatX_strY(x: float, y: str):
    return False

@define_behavior
def py_eq_strX_sintY(x: str, y: sint):
    return False

@define_behavior
def py_eq_strX_bintY(x: str, y: bint):
    return False

@define_behavior
def py_eq_strX_boolY(x: str, y: bool):
    return False

@define_behavior
def py_eq_strX_floatY(x: str, y: float):
    return False

@define_behavior
def py_eq_strX_strY(x: str, y: str):
    return py_bool_from_host_bool(py_str_to_host(x) == py_str_to_host(y))

@define_behavior
def py_ne_sintX_sintY(x: sint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_sintX_bintY(x: sint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_sintX_boolY(x: sint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_sintX_floatY(x: sint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) != py_int_to_host(x))

@define_behavior
def py_ne_sintX_strY(x: sint, y: str):
    return True

@define_behavior
def py_ne_bintX_sintY(x: bint, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_bintX_bintY(x: bint, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_bintX_boolY(x: bint, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_bintX_floatY(x: bint, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) != py_int_to_host(x))

@define_behavior
def py_ne_bintX_strY(x: bint, y: str):
    return True

@define_behavior
def py_ne_boolX_sintY(x: bool, y: sint):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_boolX_bintY(x: bool, y: bint):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_boolX_boolY(x: bool, y: bool):
    return py_bool_from_host_bool(py_int_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_boolX_floatY(x: bool, y: float):
    return py_bool_from_host_bool(py_float_to_host(y) != py_int_to_host(x))

@define_behavior
def py_ne_boolX_strY(x: bool, y: str):
    return True

@define_behavior
def py_ne_floatX_sintY(x: float, y: sint):
    return py_bool_from_host_bool(py_float_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_floatX_bintY(x: float, y: bint):
    return py_bool_from_host_bool(py_float_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_floatX_boolY(x: float, y: bool):
    return py_bool_from_host_bool(py_float_to_host(x) != py_int_to_host(y))

@define_behavior
def py_ne_floatX_floatY(x: float, y: float):
    return py_bool_from_host_bool(py_float_to_host(x) != py_float_to_host(y))

@define_behavior
def py_ne_floatX_strY(x: float, y: str):
    return True

@define_behavior
def py_ne_strX_sintY(x: str, y: sint):
    return True

@define_behavior
def py_ne_strX_bintY(x: str, y: bint):
    return True

@define_behavior
def py_ne_strX_boolY(x: str, y: bool):
    return True

@define_behavior
def py_ne_strX_floatY(x: str, y: float):
    return True

@define_behavior
def py_ne_strX_strY(x: str, y: str):
    return py_bool_from_host_bool(py_str_to_host(x) != py_str_to_host(y))

@define_behavior
def py_test_ge_sintX_sintY(x: sint, y: sint):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_sintX_bintY(x: sint, y: bint):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_sintX_boolY(x: sint, y: bool):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_sintX_floatY(x: sint, y: float):
    return py_float_to_host(y) <= py_int_to_host(x)

@define_behavior
def py_test_ge_sintX_strY(x: sint, y: str):
    raise TypeError("'>=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_ge_bintX_sintY(x: bint, y: sint):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_bintX_bintY(x: bint, y: bint):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_bintX_boolY(x: bint, y: bool):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_bintX_floatY(x: bint, y: float):
    return py_float_to_host(y) <= py_int_to_host(x)

@define_behavior
def py_test_ge_bintX_strY(x: bint, y: str):
    raise TypeError("'>=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_ge_boolX_sintY(x: bool, y: sint):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_boolX_bintY(x: bool, y: bint):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_boolX_boolY(x: bool, y: bool):
    return py_int_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_boolX_floatY(x: bool, y: float):
    return py_float_to_host(y) <= py_int_to_host(x)

@define_behavior
def py_test_ge_boolX_strY(x: bool, y: str):
    raise TypeError("'>=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_test_ge_floatX_sintY(x: float, y: sint):
    return py_float_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_floatX_bintY(x: float, y: bint):
    return py_float_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_floatX_boolY(x: float, y: bool):
    return py_float_to_host(x) >= py_int_to_host(y)

@define_behavior
def py_test_ge_floatX_floatY(x: float, y: float):
    return py_float_to_host(x) >= py_float_to_host(y)

@define_behavior
def py_test_ge_floatX_strY(x: float, y: str):
    raise TypeError("'>=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_test_ge_strX_sintY(x: str, y: sint):
    raise TypeError("'>=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_ge_strX_bintY(x: str, y: bint):
    raise TypeError("'>=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_ge_strX_boolY(x: str, y: bool):
    raise TypeError("'>=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_test_ge_strX_floatY(x: str, y: float):
    raise TypeError("'>=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_test_ge_strX_strY(x: str, y: str):
    return py_str_to_host(x) >= py_str_to_host(y)

@define_behavior
def py_test_gt_sintX_sintY(x: sint, y: sint):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_sintX_bintY(x: sint, y: bint):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_sintX_boolY(x: sint, y: bool):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_sintX_floatY(x: sint, y: float):
    return py_float_to_host(y) < py_int_to_host(x)

@define_behavior
def py_test_gt_sintX_strY(x: sint, y: str):
    raise TypeError("'>' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_gt_bintX_sintY(x: bint, y: sint):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_bintX_bintY(x: bint, y: bint):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_bintX_boolY(x: bint, y: bool):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_bintX_floatY(x: bint, y: float):
    return py_float_to_host(y) < py_int_to_host(x)

@define_behavior
def py_test_gt_bintX_strY(x: bint, y: str):
    raise TypeError("'>' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_gt_boolX_sintY(x: bool, y: sint):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_boolX_bintY(x: bool, y: bint):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_boolX_boolY(x: bool, y: bool):
    return py_int_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_boolX_floatY(x: bool, y: float):
    return py_float_to_host(y) < py_int_to_host(x)

@define_behavior
def py_test_gt_boolX_strY(x: bool, y: str):
    raise TypeError("'>' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_test_gt_floatX_sintY(x: float, y: sint):
    return py_float_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_floatX_bintY(x: float, y: bint):
    return py_float_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_floatX_boolY(x: float, y: bool):
    return py_float_to_host(x) > py_int_to_host(y)

@define_behavior
def py_test_gt_floatX_floatY(x: float, y: float):
    return py_float_to_host(x) > py_float_to_host(y)

@define_behavior
def py_test_gt_floatX_strY(x: float, y: str):
    raise TypeError("'>' not supported between instances of 'float' and 'str'")

@define_behavior
def py_test_gt_strX_sintY(x: str, y: sint):
    raise TypeError("'>' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_gt_strX_bintY(x: str, y: bint):
    raise TypeError("'>' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_gt_strX_boolY(x: str, y: bool):
    raise TypeError("'>' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_test_gt_strX_floatY(x: str, y: float):
    raise TypeError("'>' not supported between instances of 'str' and 'float'")

@define_behavior
def py_test_gt_strX_strY(x: str, y: str):
    return py_str_to_host(x) > py_str_to_host(y)

@define_behavior
def py_test_le_sintX_sintY(x: sint, y: sint):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_sintX_bintY(x: sint, y: bint):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_sintX_boolY(x: sint, y: bool):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_sintX_floatY(x: sint, y: float):
    return py_float_to_host(y) >= py_int_to_host(x)

@define_behavior
def py_test_le_sintX_strY(x: sint, y: str):
    raise TypeError("'<=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_le_bintX_sintY(x: bint, y: sint):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_bintX_bintY(x: bint, y: bint):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_bintX_boolY(x: bint, y: bool):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_bintX_floatY(x: bint, y: float):
    return py_float_to_host(y) >= py_int_to_host(x)

@define_behavior
def py_test_le_bintX_strY(x: bint, y: str):
    raise TypeError("'<=' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_le_boolX_sintY(x: bool, y: sint):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_boolX_bintY(x: bool, y: bint):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_boolX_boolY(x: bool, y: bool):
    return py_int_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_boolX_floatY(x: bool, y: float):
    return py_float_to_host(y) >= py_int_to_host(x)

@define_behavior
def py_test_le_boolX_strY(x: bool, y: str):
    raise TypeError("'<=' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_test_le_floatX_sintY(x: float, y: sint):
    return py_float_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_floatX_bintY(x: float, y: bint):
    return py_float_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_floatX_boolY(x: float, y: bool):
    return py_float_to_host(x) <= py_int_to_host(y)

@define_behavior
def py_test_le_floatX_floatY(x: float, y: float):
    return py_float_to_host(x) <= py_float_to_host(y)

@define_behavior
def py_test_le_floatX_strY(x: float, y: str):
    raise TypeError("'<=' not supported between instances of 'float' and 'str'")

@define_behavior
def py_test_le_strX_sintY(x: str, y: sint):
    raise TypeError("'<=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_le_strX_bintY(x: str, y: bint):
    raise TypeError("'<=' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_le_strX_boolY(x: str, y: bool):
    raise TypeError("'<=' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_test_le_strX_floatY(x: str, y: float):
    raise TypeError("'<=' not supported between instances of 'str' and 'float'")

@define_behavior
def py_test_le_strX_strY(x: str, y: str):
    return py_str_to_host(x) <= py_str_to_host(y)

@define_behavior
def py_test_lt_sintX_sintY(x: sint, y: sint):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_sintX_bintY(x: sint, y: bint):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_sintX_boolY(x: sint, y: bool):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_sintX_floatY(x: sint, y: float):
    return py_float_to_host(y) > py_int_to_host(x)

@define_behavior
def py_test_lt_sintX_strY(x: sint, y: str):
    raise TypeError("'<' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_lt_bintX_sintY(x: bint, y: sint):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_bintX_bintY(x: bint, y: bint):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_bintX_boolY(x: bint, y: bool):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_bintX_floatY(x: bint, y: float):
    return py_float_to_host(y) > py_int_to_host(x)

@define_behavior
def py_test_lt_bintX_strY(x: bint, y: str):
    raise TypeError("'<' not supported between instances of 'int' and 'str'")

@define_behavior
def py_test_lt_boolX_sintY(x: bool, y: sint):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_boolX_bintY(x: bool, y: bint):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_boolX_boolY(x: bool, y: bool):
    return py_int_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_boolX_floatY(x: bool, y: float):
    return py_float_to_host(y) > py_int_to_host(x)

@define_behavior
def py_test_lt_boolX_strY(x: bool, y: str):
    raise TypeError("'<' not supported between instances of 'bool' and 'str'")

@define_behavior
def py_test_lt_floatX_sintY(x: float, y: sint):
    return py_float_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_floatX_bintY(x: float, y: bint):
    return py_float_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_floatX_boolY(x: float, y: bool):
    return py_float_to_host(x) < py_int_to_host(y)

@define_behavior
def py_test_lt_floatX_floatY(x: float, y: float):
    return py_float_to_host(x) < py_float_to_host(y)

@define_behavior
def py_test_lt_floatX_strY(x: float, y: str):
    raise TypeError("'<' not supported between instances of 'float' and 'str'")

@define_behavior
def py_test_lt_strX_sintY(x: str, y: sint):
    raise TypeError("'<' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_lt_strX_bintY(x: str, y: bint):
    raise TypeError("'<' not supported between instances of 'str' and 'int'")

@define_behavior
def py_test_lt_strX_boolY(x: str, y: bool):
    raise TypeError("'<' not supported between instances of 'str' and 'bool'")

@define_behavior
def py_test_lt_strX_floatY(x: str, y: float):
    raise TypeError("'<' not supported between instances of 'str' and 'float'")

@define_behavior
def py_test_lt_strX_strY(x: str, y: str):
    return py_str_to_host(x) < py_str_to_host(y)

@define_behavior
def py_test_eq_sintX_sintY(x: sint, y: sint):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_sintX_bintY(x: sint, y: bint):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_sintX_boolY(x: sint, y: bool):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_sintX_floatY(x: sint, y: float):
    return py_float_to_host(y) == py_int_to_host(x)

@define_behavior
def py_test_eq_sintX_strY(x: sint, y: str):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_bintX_sintY(x: bint, y: sint):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_bintX_bintY(x: bint, y: bint):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_bintX_boolY(x: bint, y: bool):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_bintX_floatY(x: bint, y: float):
    return py_float_to_host(y) == py_int_to_host(x)

@define_behavior
def py_test_eq_bintX_strY(x: bint, y: str):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_boolX_sintY(x: bool, y: sint):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_boolX_bintY(x: bool, y: bint):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_boolX_boolY(x: bool, y: bool):
    return py_int_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_boolX_floatY(x: bool, y: float):
    return py_float_to_host(y) == py_int_to_host(x)

@define_behavior
def py_test_eq_boolX_strY(x: bool, y: str):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_floatX_sintY(x: float, y: sint):
    return py_float_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_floatX_bintY(x: float, y: bint):
    return py_float_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_floatX_boolY(x: float, y: bool):
    return py_float_to_host(x) == py_int_to_host(y)

@define_behavior
def py_test_eq_floatX_floatY(x: float, y: float):
    return py_float_to_host(x) == py_float_to_host(y)

@define_behavior
def py_test_eq_floatX_strY(x: float, y: str):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_strX_sintY(x: str, y: sint):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_strX_bintY(x: str, y: bint):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_strX_boolY(x: str, y: bool):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_strX_floatY(x: str, y: float):
    return py_bool_to_host_bool(False)

@define_behavior
def py_test_eq_strX_strY(x: str, y: str):
    return py_str_to_host(x) == py_str_to_host(y)

@define_behavior
def py_test_ne_sintX_sintY(x: sint, y: sint):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_sintX_bintY(x: sint, y: bint):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_sintX_boolY(x: sint, y: bool):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_sintX_floatY(x: sint, y: float):
    return py_float_to_host(y) != py_int_to_host(x)

@define_behavior
def py_test_ne_sintX_strY(x: sint, y: str):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_bintX_sintY(x: bint, y: sint):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_bintX_bintY(x: bint, y: bint):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_bintX_boolY(x: bint, y: bool):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_bintX_floatY(x: bint, y: float):
    return py_float_to_host(y) != py_int_to_host(x)

@define_behavior
def py_test_ne_bintX_strY(x: bint, y: str):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_boolX_sintY(x: bool, y: sint):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_boolX_bintY(x: bool, y: bint):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_boolX_boolY(x: bool, y: bool):
    return py_int_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_boolX_floatY(x: bool, y: float):
    return py_float_to_host(y) != py_int_to_host(x)

@define_behavior
def py_test_ne_boolX_strY(x: bool, y: str):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_floatX_sintY(x: float, y: sint):
    return py_float_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_floatX_bintY(x: float, y: bint):
    return py_float_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_floatX_boolY(x: float, y: bool):
    return py_float_to_host(x) != py_int_to_host(y)

@define_behavior
def py_test_ne_floatX_floatY(x: float, y: float):
    return py_float_to_host(x) != py_float_to_host(y)

@define_behavior
def py_test_ne_floatX_strY(x: float, y: str):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_strX_sintY(x: str, y: sint):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_strX_bintY(x: str, y: bint):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_strX_boolY(x: str, y: bool):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_strX_floatY(x: str, y: float):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_ne_strX_strY(x: str, y: str):
    return py_str_to_host(x) != py_str_to_host(y)

@define_behavior
def py_pos_sintX(x: sint):
    return x

@define_behavior
def py_pos_bintX(x: bint):
    return x

@define_behavior
def py_pos_boolX(x: bool):
    return py_int_from_host(py_int_to_host(x))

@define_behavior
def py_pos_floatX(x: float):
    return x

@define_behavior
def py_pos_strX(x: str):
    raise TypeError("bad operand type for unary +:'str'")

@define_behavior
def py_neg_sintX(x: sint):
    return py_int_from_host(-py_int_to_host(x))

@define_behavior
def py_neg_bintX(x: bint):
    return py_int_from_host(-py_int_to_host(x))

@define_behavior
def py_neg_boolX(x: bool):
    return py_int_from_host(-py_int_to_host(x))

@define_behavior
def py_neg_floatX(x: float):
    return py_float_from_host(-py_float_to_host(x))

@define_behavior
def py_neg_strX(x: str):
    raise TypeError("bad operand type for unary -:'str'")

@define_behavior
def py_invert_sintX(x: sint):
    return py_int_from_host(~py_int_to_host(x))

@define_behavior
def py_invert_bintX(x: bint):
    return py_int_from_host(~py_int_to_host(x))

@define_behavior
def py_invert_boolX(x: bool):
    return py_int_from_host(~py_int_to_host(x))

@define_behavior
def py_invert_floatX(x: float):
    raise TypeError("bad operand type for unary ~:'float'")

@define_behavior
def py_invert_strX(x: str):
    raise TypeError("bad operand type for unary ~:'str'")

@define_behavior
def py_truth_sintX(obj: sint):
    return py_bool_from_host_bool(py_int_to_host(0) != py_int_to_host(obj))

@define_behavior
def py_truth_bintX(obj: bint):
    return True

@define_behavior
def py_truth_boolX(obj: bool):
    return obj

@define_behavior
def py_truth_floatX(obj: float):
    return py_bool_from_host_bool(py_float_to_host(0.0) != py_float_to_host(obj))

@define_behavior
def py_truth_strX(obj: str):
    return py_int_from_host(py_str_len_to_host(obj)) != 0

@define_behavior
def py_test_sintX(obj: sint):
    return py_int_to_host(0) != py_int_to_host(obj)

@define_behavior
def py_test_bintX(obj: bint):
    return py_bool_to_host_bool(True)

@define_behavior
def py_test_boolX(obj: bool):
    return py_bool_to_host_bool(obj)

@define_behavior
def py_test_floatX(obj: float):
    return py_float_to_host(0.0) != py_float_to_host(obj)

@define_behavior
def py_test_strX(obj: str):
    return py_bool_to_host_bool(py_int_from_host(py_str_len_to_host(obj)) != 0)

@define_behavior
def py_descriptor_get_functionX_Y_Z(attr: function, instance, owner):
    if instance is None:
        return attr
    else:
        return alloc(method, method=attr, self=instance)

@define_behavior
def py_call_float_sintX(val: sint):
    return py_int_to_float(val)

@define_behavior
def py_call_float_bintX(val: bint):
    return py_int_to_float(val)

@define_behavior
def py_call_float_boolX(val: bool):
    return py_int_to_float(val)

@define_behavior
def py_call_float_floatX(val: float):
    return val

