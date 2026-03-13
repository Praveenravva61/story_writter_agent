from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ..tools.base_instruction import BASE_STORY_STRUCTURE
from ..tools.critic import critic_agent, approve_draft


historical_writer_agent = Agent(
    name="historical_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Historical Fiction

Additional Guidelines:

Write a story set in a believable historical era.

The setting should feel authentic, describing culture, environment,
and challenges faced during that period.

The hero should face personal struggles influenced by the historical world.

The climax should involve a decision or event that reflects the time period.

Important:
The story must be completely original.
Do NOT copy real historical stories or movies.
"""
    ),
    output_key="latest_draft"
)


