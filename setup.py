#! /usr/bin/env python

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name='pyglsl_parser',
        sources=['pyglsl_parser/pyglsl_parser.pyx',
         'glsl-parser/ast.cpp',
         'glsl-parser/lexer.cpp',
         'glsl-parser/parser.cpp',
         'glsl-parser/util.cpp'],
        language='c++',
    )
]

setup(name='pyglsl_parser',
      version='1.0.0',
      test_suite='test',
      ext_modules=cythonize(extensions))
