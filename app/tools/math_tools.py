import sympy as sp
def simplify_expression(expression: str):
    expr = sp.sympify(expression)
    result = sp.simplify(expr)
    return {
        "operation": "simplify",
        "input": expression,
        "result": str(result)
    }