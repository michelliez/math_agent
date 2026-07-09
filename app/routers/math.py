from fastapi import APIRouter
from app.schemas import MathRequest
from app.agents.math_agent import extract_math_request, answer_directly, run_math_tool, explain_tool_result, create_math_plan, execute_math_plan, explain_plan_result


router = APIRouter(prefix="/math", tags=["Math"])

@router.post("/extract")
def extract(req: MathRequest):
    result = extract_math_request(req.question)
    return result

@router.post("/ask")
def ask(req: MathRequest):
    #See if problem requires multiple steps. If yes, create a plan.
    plan = create_math_plan(req.question)
    if plan.use_plan:
        plan_result = execute_math_plan(plan)
        answer = explain_plan_result(req.question, plan_result)
        return {
            "answer": answer,
            # "execution": {
            #     "planner": plan,
            #     "plan_result": plan_result
            # }
        }
    
    #For direct answer problems:
    #Extract the type of problem
    extraction = extract_math_request(req.question)

    #For regular, general, nontool specific questions:
    if not extraction.use_tool:
        answer = answer_directly(req.question)
        return {
            # "question": req.question,
            # "use_tool": False,
            "answer": answer
        }
    #If a tool is used:
    tool_result = run_math_tool(
        operation = extraction.operation,
        expression = extraction.expression,
        variable = extraction.variable,
    )
    answer = explain_tool_result(req.question, extraction, tool_result)
    return {
        # "question": req.question,
        # "use_tool": True,
        "answer": answer,
        # "tool_result": tool_result
    }

@router.post("/plan")
def plan(req: MathRequest):
    return create_math_plan(req.question)