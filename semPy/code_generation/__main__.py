import argparse

from . import templates


def init_number_class(*, class_template, method_info, shift_method_info, division_method_info, comparison_method_info,
                      unary_method_info, binary_method_template, reflected_binary_method_template,
                      inplace_binary_method_template, shift_method_template, reflected_shift_method_template,
                      inplace_shift_method_template, division_method_template, reflected_division_method_template,
                      inplace_division_method_template, comparison_method_template, unary_method_template):
    int_methods = ""

    for semantics, data in method_info.items():
        int_methods += binary_method_template.format(**data)
        int_methods += reflected_binary_method_template.format(**data)
        int_methods += inplace_binary_method_template.format(**data)

    for semantics, data in shift_method_info.items():
        int_methods += shift_method_template.format(**data)
        int_methods += reflected_shift_method_template.format(**data)
        int_methods += inplace_shift_method_template.format(**data)

    for semantics, data in unary_method_info.items():
        int_methods += unary_method_template.format(**data)

    for semantics, data in division_method_info.items():
        int_methods += division_method_template.format(**data)
        int_methods += reflected_division_method_template.format(**data)
        int_methods += inplace_division_method_template.format(**data)

    for semantics, data in comparison_method_info.items():
        int_methods += comparison_method_template.format(**data)

    return class_template.format(methods=int_methods)


def init_str_class():
    methods = ""

    for semantics, data in templates.str_comparison_method_info.items():
        methods += templates.str_comparison_method_template.format(**data)

    return templates.class_str_template.format(methods=methods)


def generate_builtins():
    int_class = init_number_class(class_template=templates.class_int_template,
                                  method_info=templates.int_method_info,
                                  shift_method_info=templates.int_shift_method_info,
                                  division_method_info=templates.int_division_method_info,
                                  comparison_method_info=templates.int_comparison_method_info,
                                  unary_method_info=templates.int_unary_method_info,
                                  binary_method_template=templates.int_binary_method_template,
                                  reflected_binary_method_template=templates.int_reflected_binary_method_template,
                                  inplace_binary_method_template=templates.int_inplace_binary_method_template,
                                  shift_method_template=templates.int_shift_method_template,
                                  reflected_shift_method_template=templates.int_reflected_shift_method_template,
                                  inplace_shift_method_template=templates.int_inplace_shift_method_template,
                                  division_method_template=templates.int_division_method_template,
                                  reflected_division_method_template=templates.int_reflected_division_method_template,
                                  inplace_division_method_template=templates.int_inplace_division_method_template,
                                  comparison_method_template=templates.int_comparison_method_template,
                                  unary_method_template=templates.int_unary_method_template)

    bool_class = init_number_class(class_template=templates.class_bool_template,
                                   method_info=templates.bool_method_info,
                                   shift_method_info={},
                                   division_method_info={},
                                   comparison_method_info={},
                                   unary_method_info={},
                                   binary_method_template=templates.bool_binary_method_template,
                                   reflected_binary_method_template=templates.bool_reflected_binary_method_template,
                                   inplace_binary_method_template="",
                                   shift_method_template="",
                                   reflected_shift_method_template="",
                                   inplace_shift_method_template="",
                                   division_method_template="",
                                   reflected_division_method_template="",
                                   inplace_division_method_template="",
                                   comparison_method_template="",
                                   unary_method_template="")

    float_class = init_number_class(class_template=templates.class_float_template,
                                    method_info=templates.float_method_info,
                                    shift_method_info={},
                                    division_method_info=templates.float_division_method_info,
                                    comparison_method_info=templates.float_comparison_method_info,
                                    unary_method_info=templates.float_unary_method_info,
                                    binary_method_template=templates.float_binary_method_template,
                                    reflected_binary_method_template=templates.float_reflected_binary_method_template,
                                    inplace_binary_method_template=templates.float_inplace_binary_method_template,
                                    shift_method_template="",
                                    reflected_shift_method_template="",
                                    inplace_shift_method_template="",
                                    division_method_template=templates.float_division_method_template,
                                    reflected_division_method_template=templates.float_reflected_division_method_template,
                                    inplace_division_method_template=templates.float_inplace_division_method_template,
                                    comparison_method_template=templates.float_comparison_method_template,
                                    unary_method_template=templates.float_unary_method_template)

    str_class = init_str_class()

    definitions = "\n\n".join([int_class, bool_class, float_class, str_class])

    builtins = templates.builtins_template.format(definitions=definitions)

    return builtins

def generate_semantics():
    arithmetic = [templates.arithmetic_template.format(**info) for info in templates.arithmetic_info.values()]
    inplace_arithmetic = [templates.inplace_arithmetic_template.format(**info) for info in
                          templates.inplace_arithmetic_info.values()]
    unary_arithmetic = [templates.unary_arithmetic_template.format(**info) for info in
                        templates.unary_arithmetic_info.values()]
    comparison = [templates.comparison_template.format(**info) for info in templates.comparison_info.values()]
    equality = [templates.equality_template.format(**info) for info in templates.equality_info.values()]

    arithmetic_semantics = '\n\n'.join(arithmetic + inplace_arithmetic + unary_arithmetic + comparison + equality)

    semantics = templates.semantics_template.format(arithmetic=arithmetic_semantics)

    return semantics

if __name__ == '__main__':
    generators = {
        "builtins": generate_builtins,
        "semantics": generate_semantics
    }

    # Argument parsing
    parser = argparse.ArgumentParser(description="Manage Python builtins file")

    subparser = parser.add_subparsers(dest='command', required=True)

    # builtins command
    builtins_parser = subparser.add_parser('builtins', description="Initialize a builtins.py file from templates")
    builtins_parser.add_argument('-o', default=None)

    # semantics command
    semantics_parser = subparser.add_parser('semantics', description="Initialize a semantics.py file from templates")
    semantics_parser.add_argument('-o', default=None)

    args = parser.parse_args()
    command = args.command
    path = args.o

    # Generate and output code
    generate = generators[command]

    if path:
        with open(path, 'w') as f:
            f.write(generate())
    else:
        print(generate())
