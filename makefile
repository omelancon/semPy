PYTHON3 ?= python3

.PHONY: all behaviors magic_methods clean

all: behaviors

magic_methods: out/magic_methods.txt

behaviors: out/behaviors.py

clean:
	touch out/__dummy.py; rm out/*.py

out/builtins.py: semPy/code_generation/__main__.py semPy/code_generation/templates.py
	$(PYTHON3) -m semPy.code_generation builtins -o out/builtins.py

out/semantics.py: semPy/code_generation/__main__.py semPy/code_generation/templates.py
	$(PYTHON3) -m semPy.code_generation semantics -o out/semantics.py

out/behaviors.py: out/builtins.py out/semantics.py
	$(PYTHON3) -m semPy out/semantics.py out/builtins.py -o out/behaviors.py
