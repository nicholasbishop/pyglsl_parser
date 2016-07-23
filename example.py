#! /usr/bin/env python

# TODO

from pyglsl_parser.parser import parse
from argparse import ArgumentParser
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
    cli_args = parse_cli_args()
    path = cli_args.path
    shader_type = ShaderType[cli_args.shader_type]

    with open(path) as glsl_file:
        source = glsl_file.read()

    ast = parse(source, path, shader_type)
    print('functions:')
    for func in ast.functions:
        print(func)
        

if __name__ == '__main__':
    main()
