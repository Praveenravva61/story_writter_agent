from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ..tools.base_instruction import BASE_STORY_STRUCTURE


def approve_draft(tool_context:ToolContext)->dict:
    """
    call this tools to when the draft is completely meets the rubic,
     and is approved. 
    Donot call this tool if this draft fails any rubic creteria.
    
    """
    
    tool_context.actions.escalate= True
    return {"status": "approved", "message": "The draft has been approved."}


critic_agent = Agent(
    name="critic_agent",
    model="gemini-3-pro-preview",
    instruction="""
You are a professional story editor.

Evaluate the story draft using the following rubric:

STRUCTURE CHECK:
The story MUST clearly contain these 8 sections:

1. Hook
2. World Introduction
3. Hero Introduction
4. Inciting Incident
5. Conflict Escalation
6. Emotional Turning Point
7. Climax
8. Resolution

QUALITY CHECK:
- The story must feel original.
- It must match the intended genre.
- It must be emotionally engaging.
- The narrative should flow logically.

If ANY requirement fails:
Provide clear actionable feedback explaining what needs improvement.

If the story is high quality and follows all rules:
Call the approve_draft tool.

Story Draft:
{latest_draft}
""",
    tools=[FunctionTool(approve_draft)],
    output_key="latest_feedback"
)