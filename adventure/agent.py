from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ..tools.base_instruction import BASE_STORY_STRUCTURE
from ..tools.critic import critic_agent, approve_draft


#==================================================================================================
# adventure_writer_agent:
#==================================================================================================

adventure_writer_agent = Agent(
    name="adventure_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Adventure / Epic Quest

Additional Guidelines:

Create an exciting adventure story centered around exploration and discovery.

The story may include:
- ancient ruins
- lost civilizations
- hidden treasures
- dangerous environments
- rival explorers or enemies

The world should feel mysterious and full of secrets.

The hero should face escalating dangers during the journey.

The climax should involve a major discovery or heroic action.

Important:
The story must be completely original.
Do NOT copy existing adventure movies or books.
"""
    ),
    output_key="latest_draft"
)

adventure_story_pipeline = LoopAgent(
    name="adventure_story_pipeline",
    sub_agents=[
        adventure_writer_agent,
        critic_agent
    ],
    max_iterations=4
)
    