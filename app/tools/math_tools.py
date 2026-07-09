import sympy as sp


def simplify_expression(expression: str):
    expr = sp.sympify(expression)
    result = sp.simplify(expr)
    return {
        "operation": "simplify",
        "input": expression,
        "result": str(result)
    }

def derivative (expression: str, variable: str = "x"):
    x = sp.Symbol(variable)
    expr = sp.sympify(expression)
    result = sp.diff(expr, x)
    return {
        "operation": "derivative",
        "input": expression,
        "variable": variable,
        "result": str(result)
    }

def solve_equation(expression: str, variable: str = "x"):
    x = sp.Symbol(variable)
    expr = sp.sympify(expression)
    result = sp.solve(expr, x)
    return {
        "operation": "solve_equation",
        "input": expression,
        "variable": variable,
        "result": [str(r) for r in result]

    }