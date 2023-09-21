A tool to analyze Python's semantics and generate fast paths for frequently used operators and type combinations.

# Summary
In 2018, our team at Université de Montréal began researching optimizing compilers for Python. We quickly realized that one of the major obstacles to writing an optimizing Python compiler stems from its complex semantics. During our first year, we primarily focused on _getting the semantics right_, leaving little room for actual optimization.

This led to the development of executable semantics, written in Python syntax, that could be reused across different compilers. This semantics allows to skip the tedious early-stage process of implementing the semantics for each operator, along with the magic methods for each built-in type.

Moreover, having an executable semantics enables us to apply static analysis without having to hard-code the semantics into the tools. All that's required is for the tools to be able to read the semantics, which are already written in Python.

`semPy` is a tool that can interpret our executable semantics to apply optimizations such as magic method inlining, type-check removal, and boxing and unboxing removal. While these optimizations can't be applied in general, they can be applied when the type of an operand is known. In such cases, the exact magic method to call is often also known.

`semPy` generates _behaviors_, which are functions that represent fast paths for executing an operation for a given combination of types. We used semPy in our prototype Python compiler, Zipi, which in some cases outperformed even PyPy.

For more details, read the full paper: [An Executable Semantics for Faster Development of Optimizing Python Compilers](http://www.iro.umontreal.ca/~feeley/papers/MelanconFeeleySerranoSLE23.pdf)

# Usage

Semantics files are pre-generated in the `out` folder. To regenerate them use `make clean; make`.
