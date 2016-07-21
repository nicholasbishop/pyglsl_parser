# distutils: language = c++
# distutils: extra_compile_args = -fno-rtti -fno-exceptions

from libcpp cimport bool
from libcpp.vector cimport vector
from cython.operator import dereference
from pyglsl_parser.enums import ShaderType
from pyglsl_parser import lexemes
from pyglsl_parser.ast import Ast, AstFunction, AstFunctionParameter

cdef extern from '../glsl-parser/ast.h' namespace 'glsl':
    cdef cppclass astType:
        bool builtin

    cdef cppclass astBuiltin:
        int type

    cdef cppclass astStruct:
        pass

    cdef cppclass astVariable:
        char* name
        astType* baseType

    cdef cppclass astFunctionParameter:
        int storage
        int auxiliary
        int memory
        int precision

    cdef cppclass astFunction:
        astType* returnType
        char* name
        vector[astFunctionParameter*] parameters
        bool isPrototype

    cdef cppclass astTU:
        astTU(int type)
        vector[astFunction*] functions
        int type


cdef extern from '../glsl-parser/parser.h' namespace 'glsl':
    cdef cppclass parser:
        parser(const char* source, const char* fileName)
        astTU* parse(int type)
        const char* error() const


cdef convert_builtin_type(astBuiltin* c_builtin):
    keyword = lexemes.Keyword(c_builtin.type).name
    type_name = lexemes.Typename[keyword]

    return type_name


cdef convert_struct_type(astStruct* c_struct):
    raise NotImplementedError()


cdef convert_type(astType* c_type):
    if c_type.builtin:
        return convert_builtin_type(<astBuiltin*>(c_type))
    else:
        return convert_struct_type(<astStruct*>(c_type))


cdef convert_function_parameter(astFunctionParameter* c_param):
    c_var = <astVariable*>(c_param)
    # TODO(nicholasbishop): other fields
    return AstFunctionParameter(name=c_var.name.decode(),
                                base_type=convert_type(c_var.baseType))


cdef convert_function(astFunction* c_func):
    params = [convert_function_parameter(par) for par in c_func.parameters]

    func = AstFunction(name=c_func.name.decode(),
                       return_type=convert_type(c_func.returnType),
                       parameters=params,
                       is_prototype=c_func.isPrototype)
    # TODO: other fields
    return func


cdef convert_ast(astTU* c_ast):
    ast = Ast(c_ast.type)
    for c_func in c_ast.functions:
        ast.functions.append(convert_function(c_func))
    return ast


cdef class Parser:
    cdef parser* c_parser

    def __cinit__(self, source, filename=''):
        self.c_parser = new parser(source.encode(), filename.encode())

    def __dealloc__(self):
        del self.c_parser

    def parse(self, shader_type=ShaderType.Vertex):
        c_ast = self.c_parser.parse(shader_type.value)
        if c_ast:
            return convert_ast(c_ast)
        else:
            return None

    def error(self):
        return self.c_parser.error().decode()
