"""GLSL shader types."""

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
