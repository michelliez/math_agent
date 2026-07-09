from pydantic import BaseModel

class MathRequest(BaseModel):
    question: str

class MathExtraction(BaseModel):
    use_tool: bool
    operation: str
    expression: str | None = None
    variable: str | None = "x"
    lower_bound: str | int | float | None = None
    upper_bound: str | int | float | None = None
    approaches: str | None = None
    direction: str | None = None


class MathPlanStep(BaseModel):
    step_number: int
    operation: str
    expression: str | None = None
    variable: str = "x"
    input_source: str = "original_expression"

class MathPlan(BaseModel):
    use_plan: bool
    goal: str
    original_expression: str
    variable: str = "x"
    steps: list[MathPlanStep]