from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ..tools.base_instruction import BASE_STORY_STRUCTURE
from ..tools.critic import critic_agent, approve_draft


#==================================================================================================
# fantasy_writer_agent:
#==================================================================================================


fantasy_writer_agent = Agent(
    name="fantasy_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Fantasy

Additional Guidelines:

Create an imaginative fantasy world filled with wonder and mystery.

The story may include:
- magical kingdoms
- mythical creatures
- ancient prophecies
- lost artifacts
- legendary warriors

Worldbuilding should feel rich and immersive.

The hero should feel significant to the world's fate.

The climax should involve an epic magical or heroic confrontation.

Important:
The story must be completely original.
Do NOT copy existing fantasy stories or movies.
"""
    ),
    output_key="latest_draft"
)
fantasy_story_pipeline = LoopAgent(
    name="fantasy_story_pipeline",
    sub_agents=[
        fantasy_writer_agent,
        critic_agent
    ],
    max_iterations=4
)