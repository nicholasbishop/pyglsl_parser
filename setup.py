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
      version='0.5.5',
      test_suite='test',
      description='Python wrapper around glsl-parser',
      url='https://github.com/nicholasbishop/pyglsl_parser',
      author='Nicholas Bishop',
      author_email='nicholasbishop@gmail.com',
      ext_modules=cythonize(extensions))
