# pylint: disable=missing-docstring

from unittest import TestCase

from pyglsl_parser.parser import Parser
from pyglsl_parser.lexemes import Typename
from pyglsl_parser.ast import AstBuiltin, AstFunction

class TestParser(TestCase):
    def test_simple_error(self):
        """Test parse error."""
        parser = Parser('x', 'myfile')
        ast = parser.parse()
        self.assertIs(ast, None)
        expected_err = 'myfile:1:2: error: premature end of file'
        self.assertEqual(parser.error(), expected_err)

    def test_simple_main(self):
        """Test empty main function."""
        ast = Parser('void main() {}').parse()
        self.assertEqual(ast.functions, [
            AstFunction(name='main',
                        return_type=AstBuiltin(Typename.void),
                        is_prototype=False)
        ])

    def test_return_type(self):
        """Test that a function return type is parsed."""
        ast = Parser('int myFunc();').parse()
        self.assertEqual(ast.functions, [
            AstFunction(name='myFunc',
                        return_type=AstBuiltin(Typename.int))
        ])

    # TODO(nicholasbishop): reenable
    # def test_parameters(self):
    #     """Test that function parameters are parsed."""
    #     ast = Parser('int myFunc(vec3 foo, mat4 bar);').parse()
    #     func = ast.functions[0]
    #     self.assertEqual(func.parameters, (
    #         FunctionParameter('foo', Typename.vec3)
    #     ))
