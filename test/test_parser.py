# pylint: disable=missing-docstring

from unittest import TestCase

from pyglsl_parser.parser import Parser
from pyglsl_parser.shader_type import ShaderType

class TestParser(TestCase):
    def test_simple_error(self):
        """Test parse error."""
        text = 'x'
        parser = Parser(text, 'myfile')
        ast = parser.parse(ShaderType.Vertex)
        self.assertIs(ast, None)
        expected_err = 'myfile:1:2: error: premature end of file'
        self.assertEqual(parser.error(), expected_err)

    def test_simple_main(self):
        """Test empty main function."""
        text = 'void main() {}'
        parser = Parser(text, 'myfile')
        ast = parser.parse(ShaderType.Vertex)
        functions = [str(func) for func in ast.functions()]
        self.assertEqual(functions, [
            'void main(){...}'
        ])
