import argparse
from .compute_behaviors import compute_behaviors

parser = argparse.ArgumentParser(description="Generate zipi decision tree and behavior functions")
parser.add_argument('semantics')
parser.add_argument('builtins')
parser.add_argument('-modules', nargs="+", default=[])
parser.add_argument('-o', default=None)
parser.add_argument('--int-maxsize', dest='int_maxsize', type=int, default=-1)

args = parser.parse_args()
semantics_file = args.semantics
builtins_file = args.builtins
path = args.o
more_modules = args.modules
int_maxsize = args.int_maxsize

# TODO: unused for now
if int_maxsize != -1:
    INT_MAXSIZE = int_maxsize

if path:
    with open(path, 'w') as f:
        f.write(compute_behaviors(semantics_file, builtins_file, more_modules))
else:
    print(compute_behaviors(semantics_file, builtins_file, more_modules))
