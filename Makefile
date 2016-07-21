lint:
	venv/bin/pylint \
		--reports=no \
		--output-format=parseable \
		--disable=locally-disabled \
		*.py \
		pyglsl_parser \
		test

.PHONE: lint
