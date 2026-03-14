from google.adk.agents import Agent,LoopAgent, LlmAgent,LoopAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft

drama_writer_agent = Agent(
    name="drama_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Drama

Additional Guidelines:

Write a deeply emotional story focused on human relationships and personal struggles.

The story should explore themes such as:
- family conflicts
- personal growth
- moral decisions
- emotional healing

The emotional turning point should reveal an important realization for the hero.

The climax should involve a powerful emotional decision.

Important:
The story must be completely original.
Do NOT copy existing drama stories.
"""
    ),
    output_key="latest_draft"
)

drama_story_pipeline = LoopAgent(
    name="drama_story_pipeline",
    sub_agents=[
        drama_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)