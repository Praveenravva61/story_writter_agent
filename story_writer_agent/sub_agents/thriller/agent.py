from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft
from config import FAST_MODEL, PRO_MODEL



thriller_writer_agent = Agent(
    name="thriller_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Thriller

Additional Guidelines:

Write a suspenseful thriller story filled with tension and high stakes.

The story should include:
- danger or urgent threats
- escalating tension
- unexpected twists

The conflict escalation should constantly increase pressure on the hero.

The climax should involve a high-risk confrontation or critical decision.

Important:
The story must be completely original.
Do NOT copy existing thriller movies or books.
"""
    ),
    output_key="latest_draft"
)

thriller_story_pipeline = LoopAgent(
    name="thriller_story_pipeline",
    sub_agents=[
        thriller_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)