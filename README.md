# pyglsl_parser

Python wrapper around [glsl-parser](https://github.com/graphitemaster/glsl-parser)

## License

MIT License (MIT), same as glsl-parser.

## Implementation

The glsl-parser code is wrapped via Cython in [pyglsl_parser/parser.pyx](pyglsl_parser/parser.pyx). Some Python enums are automatically generated from a C header with [gen_enums.py](gen_enums.py).
