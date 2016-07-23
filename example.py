#! /usr/bin/env python

"""Demonstration of the pyglsl_parser API."""

from argparse import ArgumentParser

from pyglsl_parser import parse
from pyglsl_parser.enums import ShaderType


def parse_cli_args():
    """Return parsed command-line arguments."""
    parser = ArgumentParser(description='parse and summarize a GLSL file')
    parser.add_argument('path')
    shader_type_names = [member.name for member in ShaderType]
    parser.add_argument('shader_type', nargs='?',
                        choices=shader_type_names,
                        default=ShaderType.Fragment.name)
    return parser.parse_args()


def main():
    """Parse and summarize a GLSL file."""
    cli_args = parse_cli_args()
    path = cli_args.path
    shader_type = ShaderType[cli_args.shader_type]

    # Read in the source code
    with open(path) as glsl_file:
        source = glsl_file.read()

    # Parse the source code
    ast = parse(source, path, shader_type)

    # Summarize
    print('functions:')
    for func in ast.functions:
        print(func)


if __name__ == '__main__':
    main()
