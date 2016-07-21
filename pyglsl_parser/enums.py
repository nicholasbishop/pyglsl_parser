# pylint: disable=missing-docstring

from enum import Enum, unique

@unique
class ShaderType(Enum):
    """GLSL shader types."""
    Compute = 0
    Vertex = 1
    TessControl = 2
    TessEvaluation = 3
    Geometry = 4
    Fragment = 5


@unique
class StorageQualifier(Enum):
    # pylint: disable=invalid-name
    Const = 0
    In = 1
    Out = 2
    InOut = 3
    Attribute = 4
    Uniform = 5
    Varying = 6
    Buffer = 7
    Shared = 8


@unique
class AuxiliaryStorageQualifier(Enum):
    Centroid = 0
    Sample = 1
    Patch = 2


@unique
class MemoryQualifier(Enum):
    Coherent = 1 << 0
    Volatile = 1 << 1
    Restrict = 1 << 2
    ReadOnly = 1 << 3
    WriteOnly = 1 << 4
