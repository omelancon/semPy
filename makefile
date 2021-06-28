PYTHON3 ?= python3

.PHONY: all behaviors magic_methods clean

all: magic_methods behaviors

magic_methods: out/magic_methods.txt

behaviors: out/behaviors.py

clean:
	rm out/*

out/builtins.py: code_generation/__main__.py code_generation/templates.py
	$(PYTHON3) -m code_generation builtins -path out/builtins.py

out/semantics.py: code_generation/__main__.py code_generation/templates.py
	$(PYTHON3) -m code_generation semantics -path out/semantics.py

out/behaviors.py: out/builtins.py out/semantics.py
	$(PYTHON3) compute_behaviors.py out/semantics.py out/builtins.py -path out/behaviors.py

out/magic_methods.txt: out/builtins.py out/semantics.py
	$(PYTHON3) magic_methods_usage.py out/semantics.py -path out/magic_methods.txt
