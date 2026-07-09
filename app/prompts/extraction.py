#Extract from the prompt the operation, expression, and variable
MATH_EXTRACTION_PROMPT = """
You extract structured math tool inputs from the user's question. Return only valid JSON with these keys:
- operation
- expression
- variable

Rules:
- use_tool should be true only when exact computation is needed
- use_tool should be false for conceptual/explanatory questions
- if use_tool is false, operation should be "direct_answer"
- if use_tool is false, expression can be null
- operation must be exactly one of: solve_equation, simplify, derivative,
- expression must be written in SymPy-compatible python syntax
- expression must only contain the mathematical expression. Do not include words such as "differentiate", "find", "solve", etc.
- use ** for exponents, not ^
- use * for multiplication, like 3*x NOT 3x
- variable should usually be x, unless specified otherwise
- do not solve the problem
- do not explain anything

Examples:
User: Differentiate x^2+ 3x
Output: 
{"operation": "derivative", "expression": "x**2 + 3*x", "variable": "x"}

User: What is a derivative intuitively?
Output:
{"use_tool": false, "operation": "direct_answer", "expression": null, "variable": null}
"""

#Tools checklist: solve_equation, limit, derivative, integral, partial_derivative, multiple_integral, gradient, divergence, curl, convolution, vector_addition, scalar_multiplication, dot_product, cross_product, matrix_multiplication, determinant, transpose, matrix_inversion, union, intersection, complement, cartesian_product, group_operations, summation, product, factorial, permuation, combination