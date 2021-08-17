from itertools import product


def get_behavior_name(prefix, types):
    type_signature = '_'.join(t + id_ for t, id_ in zip(['' if t == "unknown" else t for t in types], 'XYZWABCDEF'))
    return f"{prefix}_{type_signature}"


class Specializations:
    def __init__(self, module, function, types, prefix, as_test):
        self.module = module
        self.function = function
        self.types = [ts if isinstance(ts, (list, tuple)) else [ts] for ts in types]
        if prefix is None:
            if as_test:
                self.prefix = f"py_test_{function}" if prefix is None else prefix
            else:
                self.prefix = f"py_{function}" if prefix is None else prefix
        else:
            self.prefix = prefix
        self.as_test = as_test

    def __iter__(self):
        prefix = self.prefix

        for type_combination in product(*self.types):
            yield get_behavior_name(prefix, type_combination), type_combination


def maker_specializations_adder(module_name, lst):
    def add_specializations(name, types, prefix=None, as_test=False):
        lst.append(Specializations(module_name, name, types, prefix, as_test))
    return add_specializations
