#Add tools here, then update - operation must be one of: ___ in prompts/planning.py

from app.tools.algebra import (
    solve_equation,
    simplify_expression,
)

from app.tools.calculus import (
    derivative, integral
)

TOOLS = {
    "simplify": {
        "function": simplify_expression,
        "category": "algebra",
        "description": "Simplify a symbolic mathematical expression.",
        "planner_enabled": True,
    },
    "solve_equation": {
        "function": solve_equation,
        "category": "algebra",
        "description": "Solve a symbolic equation written as expression = 0.",
        "planner_enabled": True,
    },
    "derivative": {
        "function": derivative,
        "category": "calculus",
        "description": "Compute the derivative of a symbolic expression.",
        "planner_enabled": True,
    },
    "integral": {
        "function": integral,
        "category": "calculus",
        "description": "Compute the integral of a symbolic expression",
        "planner_enabled": True,
    }
}