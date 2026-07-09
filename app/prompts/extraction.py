#Extract from the prompt the operation, expression, and variable
MATH_EXTRACTION_PROMPT = """
You extract structured math tool inputs from the user's question. Return only valid JSON with these possible keys:
- operation
- expression
- variable
- lower_bound
- upper_bound
- approaches
- direction

Rules:
- use_tool should be true only when exact computation is needed
- use_tool should be false for conceptual/explanatory questions
- if use_tool is false, operation should be "direct_answer"
- if use_tool is false, expression can be null
- operation may be exactly one of: solve_equation, simplify, limit, derivative, integral, partial_derivative, multiple_integral, gradient, divergence, curl, convolution, vector_addition, scalar_multiplication, dot_product, cross_product, matrix_multiplication, determinant, transpose, matrix_inversion, union, intersection, complement, cartesian_product, group_operations, summation, product, factorial, permuation, combination
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

User: Find the integral of 3x^2
Output:
{"use_tool": true, "operation": "integral", "expression": "3*x**2", "variable": "x"}

User: Find the integral of 3x^2 from 2 to 5
Output:
{"use_tool": true, "operation": "integral", "expression": "3*x**2", "variable": "x", "lower_bound": 2, "upper_bound": 5}
"""