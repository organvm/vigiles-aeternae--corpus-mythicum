.PHONY: test

test:
	test -f README.md
	python3 -m unittest discover -s tests
