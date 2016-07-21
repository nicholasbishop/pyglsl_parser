# distutils: language = c++
# distutils: extra_compile_args = -fno-rtti -fno-exceptions

from libcpp cimport bool
from libcpp.vector cimport vector
from cython.operator import dereference
from pyglsl_parser.shader_type import ShaderType
from pyglsl_parser import lexemes


cdef extern from '../glsl-parser/ast.h' namespace 'glsl':
    cdef cppclass astType:
        bool builtin

    cdef cppclass astBuiltin:
        int type

    cdef cppclass astFunction:
        char* name
        astType* returnType
        bool isPrototype

    cdef cppclass astTU:
        astTU(int type)
        vector[astFunction*] functions


cdef extern from '../glsl-parser/parser.h' namespace 'glsl':
    cdef cppclass parser:
        parser(const char* source, const char* fileName)
        astTU* parse(int type)
        const char* error() const


cdef class Parser:
    cdef parser* c_parser

    def __cinit__(self, source, filename=''):
        self.c_parser = new parser(source.encode(), filename.encode())

    # def __dealloc__(self):
    #     del self.c_parser

    def parse(self, shader_type=ShaderType.Vertex):
        c_ast = self.c_parser.parse(shader_type.value)
        if c_ast:
            ast = Ast()
            ast.c_ast = c_ast
            return ast
        else:
            return None

    def error(self):
        return self.c_parser.error().decode()


cdef class Ast:
    cdef astTU* c_ast

    def functions(self):
        for c_function in self.c_ast.functions:
            func = Function()
            func.c_function = c_function
            yield func


cdef class Type:
    cdef astType* c_type

    def builtin(self):
        return self.c_type.builtin

    def __repr__(self):
        if self.builtin():
            c_builtin = <astBuiltin*>(self.c_type)
            return lexemes.Keyword(c_builtin.type).name
        else:
            raise NotImplementedError()


cdef class Function:
    cdef astFunction* c_function

    def name(self):
        return self.c_function.name.decode()

    def is_prototype(self):
        return self.c_function.isPrototype

    def return_type(self):
        typ = Type()
        typ.c_type = self.c_function.returnType
        return typ

    def __repr__(self):
        body = ';' if self.is_prototype() else '{...}'
        return '{ret} {name}(){body}'.format(ret=self.return_type(),
                                             name=self.name(),
                                             body=body)
