from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft


#==================================================================================================
# mystery_writer_agent:
#==================================================================================================
mystery_writer_agent = Agent(
    name="mystery_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Mystery

Additional Guidelines:

Write an intriguing mystery story centered around a puzzle or hidden truth.

The story should include:
- a mysterious event or disappearance
- subtle clues placed throughout the story
- investigation or discovery by the hero

The emotional turning point should reveal a critical clue.

The climax should uncover the hidden truth behind the mystery.

Important:
The story must be completely original.
Do NOT copy existing detective stories.
"""
    ),
    output_key="latest_draft"
)

mystery_story_pipeline = LoopAgent(
    name="mystery_story_pipeline",
    sub_agents=[
        mystery_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)