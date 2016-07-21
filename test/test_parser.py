# pylint: disable=missing-docstring

from unittest import TestCase

from pyglsl_parser.parser import Parser
from pyglsl_parser.lexemes import Typename

class TestParser(TestCase):
    def test_simple_error(self):
        """Test parse error."""
        parser = Parser('x')
        ast = parser.parse()
        self.assertIs(ast, None)
        expected_err = 'myfile:1:2: error: premature end of file'
        self.assertEqual(parser.error(), expected_err)

    def test_simple_main(self):
        """Test empty main function."""
        ast = Parser('void main() {}').parse()
        functions = [str(func) for func in ast.functions()]
        self.assertEqual(functions, [
            'void main(){...}'
        ])

    def test_return_type(self):
        """Test that a function return type is parsed."""
        ast = Parser('int myFunc();').parse()
        func = next(ast.functions())
        self.assertEqual(func.return_type, Typename.int)
