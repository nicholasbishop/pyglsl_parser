#! /usr/bin/env python

# pylint: disable=invalid-name,missing-docstring

import platform

from setuptools import setup
from setuptools.extension import Extension
from Cython.Build import cythonize


if platform.system() == 'Windows':
    extra_compile_args = ['/GR-']
else:
    extra_compile_args = ['-fno-rtti', '-fno-exceptions']

extensions = [
    Extension(
        name='pyglsl_parser.parser',
        sources=['compat.cpp',
                 'pyglsl_parser/parser.pyx',
                 'glsl-parser/ast.cpp',
                 'glsl-parser/lexer.cpp',
                 'glsl-parser/parser.cpp',
                 'glsl-parser/util.cpp'],
        language='c++',
        extra_compile_args=extra_compile_args,
    )
]

setup(name='pyglsl_parser',
      packages=['pyglsl_parser'],
      version='0.6.2',
      test_suite='test',
      description='Python wrapper around glsl-parser',
      url='https://github.com/nicholasbishop/pyglsl_parser',
      author='Nicholas Bishop',
      author_email='nicholasbishop@gmail.com',
      ext_modules=cythonize(extensions))
