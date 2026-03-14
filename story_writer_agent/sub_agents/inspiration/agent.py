from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft

inspirational_writer_agent = Agent(
    name="inspirational_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Inspirational / Sports

Additional Guidelines:

Write an uplifting story about perseverance and personal growth.

The story may involve:
- sports competitions
- personal achievements
- overcoming societal or personal obstacles

The hero should struggle against difficult odds.

The climax should involve a defining moment where the hero proves their determination.

The resolution should leave the reader feeling inspired.

Important:
The story must be completely original.
Do NOT copy existing inspirational stories.
"""
    ),
    output_key="latest_draft"
)

inspirational_story_pipeline = LoopAgent(
    name="inspirational_story_pipeline",
    sub_agents=[
        inspirational_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)