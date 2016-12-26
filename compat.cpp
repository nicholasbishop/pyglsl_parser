#include "glsl-parser/ast.h"

#ifdef _MSC_VER

#endif

namespace glsl {
	template<>
	void astNode<glsl::astFunction>::operator delete(void *) {
	}

	template<>
	void astNode<glsl::astVariable>::operator delete(void *) {
	}
}
