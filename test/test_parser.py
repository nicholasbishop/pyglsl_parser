# pylint: disable=missing-docstring

from unittest import TestCase

from pyglsl_parser import ParseError, parse
from pyglsl_parser.lexemes import Typename
from pyglsl_parser.ast import AstFunction, AstFunctionParameter

class TestParser(TestCase):
    def test_simple_error(self):
        """Test parse error."""
        with self.assertRaises(ParseError):
            try:
                parse('x', 'myfile')
            except ParseError as err:
                expected_err = 'myfile:1:2: error: premature end of file'
                self.assertEqual(err.full_error, expected_err)
                raise

    def test_simple_main(self):
        """Test empty main function."""
        ast = parse('void main() {}')
        self.assertEqual(ast.functions, [
            AstFunction(name='main',
                        return_type=Typename.void,
                        is_prototype=False)
        ])

    def test_return_type(self):
        """Test that a function return type is parsed."""
        ast = parse('int myFunc();')
        self.assertEqual(ast.functions, [
            AstFunction(name='myFunc',
                        return_type=Typename.int)
        ])

    def test_parameters(self):
        """Test that function parameters are parsed."""
        ast = parse('int myFunc(vec3 foo, mat4 bar);')
        self.assertEqual(ast.functions, [
            AstFunction(name='myFunc',
                        return_type=Typename.int,
                        parameters=[
                            AstFunctionParameter(name='foo',
                                                 base_type=Typename.vec3),
                            AstFunctionParameter(name='bar',
                                                 base_type=Typename.mat4)
                        ])
        ])

    def test_multiple_prototypes(self):
        """Test that multiple prototypes are parsed."""
        ast = parse('''void func1();
void func2();
void func3();''')
        self.assertEqual(ast.functions, [
            AstFunction(name='func1', return_type=Typename.void),
            AstFunction(name='func2', return_type=Typename.void),
            AstFunction(name='func3', return_type=Typename.void),
        ])
