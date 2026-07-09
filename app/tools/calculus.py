import sympy as sp

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

def integral (expression: str, variable: str = "x", lower_bound: str | None = None, upper_bound: str | None = None):
    x = sp.Symbol(variable)
    expr = sp.sympify(expression)
    if lower_bound is None or upper_bound is None: 
        result = sp.integrate(expr, x)
        integral_type = "indefinite"
    else:
        result = sp.integrate(
            expr, 
            (x, sp.sympify(lower_bound), sp.sympify(upper_bound))
        )
        integral_type = "definite"
    return {
        "operation": "integral",
        "type": integral_type,
        "input": expression,
        "variable": variable,
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "result": str(result)

    }