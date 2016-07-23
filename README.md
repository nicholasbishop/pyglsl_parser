# pyglsl_parser

Python wrapper around [glsl-parser](https://github.com/graphitemaster/glsl-parser)

## Quick start

```python
from pyglsl_parser import parse
ast = parse('void main();')
print(ast.functions)
# Output: [void main();]
```

Try [example.py](example.py) to see it run.

## License

MIT License (MIT), same as glsl-parser.

## Implementation

The glsl-parser code is wrapped via Cython in [pyglsl_parser/parser.pyx](pyglsl_parser/parser.pyx). Some Python enums are automatically generated from a C header with [gen_enums.py](gen_enums.py).
