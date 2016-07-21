lint:
	venv/bin/pylint \
		--reports=no \
		--output-format=parseable \
		*.py \
		pyglsl_parser \
		test

.PHONE: lint
