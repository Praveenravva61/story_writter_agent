from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft


#==================================================================================================
# thriller_writer_agent:    
#==================================================================================================
romance_writer_agent = Agent(
    name="romance_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Romance

Additional Guidelines:

Write a heartfelt romantic story focused on emotional connection between characters.

The story should include:
- believable human emotions
- meaningful interactions between characters
- internal struggles related to love or trust

The conflict should arise from emotional challenges such as:
- past heartbreak
- personal ambitions
- misunderstandings
- life circumstances

The emotional turning point should reveal something vulnerable about the characters.

The climax should involve an important decision about love.

The resolution should feel emotionally satisfying and meaningful.

Important:
The story must be completely original.
Do NOT copy existing romance movies or books.
"""
    ),
    output_key="latest_draft"
)


romance_story_pipeline = LoopAgent(
    name="romance_story_pipeline",
    sub_agents=[
        romance_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)