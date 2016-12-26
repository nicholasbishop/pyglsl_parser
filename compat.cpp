#include "glsl-parser/ast.h"

#ifdef _MSC_VER

// Fix for https://github.com/nicholasbishop/pyglsl_parser/issues/1
namespace glsl {
	template<>
	void astNode<glsl::astFunction>::operator delete(void *) {
	}

	template<>
	void astNode<glsl::astVariable>::operator delete(void *) {
	}
}

#endif  // _MSC_VER
