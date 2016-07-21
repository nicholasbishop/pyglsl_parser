#! /usr/bin/env python

# pylint: disable=invalid-name,missing-docstring

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name='pyglsl_parser.parser',
        sources=['pyglsl_parser/parser.pyx',
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
