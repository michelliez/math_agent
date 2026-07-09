from app.schemas import MathExtraction, MathPlan
from app.call_ai_hub import call_ai_hub
from app.prompts.extraction import MATH_EXTRACTION_PROMPT
from app.prompts.direct_answer import DIRECT_ANSWER_PROMPT
from app.prompts.explanation import TOOL_EXPLANATION_PROMPT, PLAN_EXPLANATION_PROMPT
from app.prompts.planning import MATH_PLANNER_PROMPT

from app.tools.math_tools import derivative, simplify_expression, solve_equation


def extract_math_request(question: str) -> MathExtraction:
    extraction = call_ai_hub(
        system_prompt=MATH_EXTRACTION_PROMPT,
        user_prompt=question,
        response_model=MathExtraction
        )
    return extraction

#Identify the operation
def classify_intent(question: str):
    q = question.lower()
    operations = {
        "simplify": ["simplify", "simplest", "simplest form", "simple"],
        "solve_equation": ["solve", "solve equation", "answer", "find"],
        "derivative": ["differentiate", "derivative", "d/dx", "dx/dy", "f'", "d/d"]

    }
    for operation in operations:
        for word in operations[operation]:
            if word in q:
                return {
                    "operation": operation
                }
    return {
        "operation": "unknown"
    }


#Use tools
def run_math_tool(operation: str, expression: str, variable: str | None = "x"):
    if operation == "derivative":
        return derivative(expression, variable or "x")
    if operation == "simplify":
        return simplify_expression(expression)
    if operation == "solve_equation":
        return solve_equation(expression, variable or "x")
    return {
        "error": f"No tool implemented for operation: {operation}"
    }

#Answer general questions directly
def answer_directly(question: str) -> str:
    return call_ai_hub(
        system_prompt=DIRECT_ANSWER_PROMPT,
        user_prompt=question
    )

#Explain tool outputs clearly
def explain_tool_result(question: str, extraction, tool_result: dict) -> str:
    return call_ai_hub(
        system_prompt=TOOL_EXPLANATION_PROMPT,
        user_prompt= f"""
        Original question: {question}

        The verified tool output is:
        Operation: {tool_result["operation"]}
        Expression: {tool_result["input"]}
        Result: {tool_result["result"]}

        Explain this verified result.
        """
    )

#LLM Creates math plan to solve
def create_math_plan(question: str) -> MathPlan:
    return call_ai_hub(
        system_prompt=MATH_PLANNER_PROMPT,
        user_prompt=question,
        response_model=MathPlan
    )

#Execute created plan
def execute_math_plan(plan: MathPlan):
    results = []
    previous_result = None

    for step in plan.steps:
        if step.input_source == "original_expression":
            expression = plan.original_expression
        elif step.input_source == "previous_result":
            expression = previous_result
        else:
            return {
                "error": f"Unknown input_source: {step.input_source}"
            }
        tool_result = run_math_tool(
            operation = step.operation,
            expression=expression,
            variable = step.variable
        )
        results.append({
            "step_number": step.step_number,
            "operation": step.operation,
            "input": expression,
            "output": tool_result
        })
        previous_result = tool_result["result"]
        return {
            "goal": plan.goal,
            "original_expression": plan.original_expression,
            "steps": results,
            "final_result": previous_result
        }

#Explain plan
def explain_plan_result(question: str, plan_result: dict) -> str:
    return call_ai_hub(
        system_prompt=PLAN_EXPLANATION_PROMPT,
        user_prompt=f"""
        Original question: {question}
        Verified plan execution: {plan_result}
        """
    )