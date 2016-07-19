from unittest import TestCase

from pyglsl_parser import Parser, ShaderType

class TestParser(TestCase):
    def test_simple_error(self):
        text = 'x'
        parser = Parser(text, 'myfile')
        ast = parser.parse(ShaderType.Vertex)
        self.assertIs(ast, None)
        expected_err = 'myfile:1:2: error: premature end of file'
        self.assertEqual(parser.error(), expected_err)

    def test_simple_main(self):
        text = 'void main() {}'
        parser = Parser(text, 'myfile')
        ast = parser.parse(ShaderType.Vertex)
        # TODO(nicholasbishop): add asserts, remove debug print
        print(list(ast.functions()))
        
