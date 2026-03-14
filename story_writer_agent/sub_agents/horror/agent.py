from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft


#==================================================================================================
# horror_writer_agent:
#==================================================================================================
horror_writer_agent = Agent(
    name="horror_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Horror

Additional Guidelines:

Write a chilling horror story that creates fear and suspense.

The story may include:
- supernatural entities
- unexplained phenomena
- psychological terror
- isolated environments

The atmosphere should feel eerie and tense.

The climax should reveal the true nature of the horror.

Important:
The story must be completely original.
Do NOT copy existing horror stories or movies.
"""
    ),
    output_key="latest_draft"
)

horror_story_pipeline = LoopAgent(
    name="horror_story_pipeline",
    sub_agents=[
        horror_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)