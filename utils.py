from code_generation import templates


def get_type_name(obj):
    return type(obj).__name__


def get_type_alias(type_name):
    return "int" if type_name in int_specialized_types else type_name


function = type(lambda: None)

instances = [1, 1.0, True, "foo", lambda: None]
types = [get_type_name(i) for i in instances]
int_specialized_types = ['sint', 'bint']
types += int_specialized_types


class Any:
    def __eq__(self, o):
        return True

    def __ne__(self, o):
        return False


# Replace 'int' by 'sint' and 'bint'
types_without_int = [t for t in types if t != 'int']

# Semantics which should be converted to behaviors
target_semantics = [*templates.arithmetic_info,
                    *templates.inplace_arithmetic_info,
                    *templates.comparison_info,
                    *templates.equality_info,
                    *templates.unary_arithmetic_info,
                    "truth",
                    "test",
                    "descriptor_get"]

# Specific semantics cases to skip
# Those are cases too complex for partial evaluation and which
# would yield no significant improvements
binary_skip = [("mod", "str", Any()),
               ("imod", "str", Any())]
