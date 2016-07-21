"""GLSL abstract syntax tree

Naming:

Class names are the same as the C++ classes except the first letter
is capitalized. Fields are generally the same name, except that
"type" has been renamed to "kind" to avoid shadowing the Python
builtin.

Initialization:

All fields are initialized in the constructor. Most are initialized to
|None| to indicate no value has been set yet. Boolean values are
initialized to False and list types are initialized to an empty list.
"""

# pylint: disable=missing-docstring

from enum import Enum, unique

class EqualityMixin(object):
    def __eq__(self, other):
        if type(other) is not type(self):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class AstBuiltin(EqualityMixin):
    def __init__(self, type_name):
        self.type_name = type_name

    def __repr__(self):
        return self.type_name.name


class AstStruct(EqualityMixin):
    def __init__(self):
        self.name = None


class AstVariable(EqualityMixin):
    def __init__(self):
        self.name = None
        self.base_type = None
        self.is_array = False
        self.is_precise = False
        self.array_sizes = []


class AstFunctionParameter(AstVariable):
    def __init__(self):
        self.storage = None
        self.auxiliary = None
        self.memory = None
        self.precision = None


class AstFunction(EqualityMixin):
    def __init__(self, name, return_type, is_prototype=True):
        self.return_type = return_type
        self.name = name
        self.parameters = []
        self.statements = []
        self.is_prototype = is_prototype

    def __repr__(self):
        body = ';' if self.is_prototype else '{...}'
        return '{ret} {name}(){body}'.format(ret=self.return_type,
                                             name=self.name,
                                             body=body)


class Ast(EqualityMixin):
    @unique
    class Kind(Enum):
        Compute = 0
        Vertex = 1
        TessControl = 2
        TessEvaluation = 3
        Geometry = 4
        Fragment = 5

    def __init__(self, kind):
        self.kind = kind

        self.functions = []
        self.types = []
        self.global_variables = []
