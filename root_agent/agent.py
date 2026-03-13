from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ..tools.base_instruction import BASE_STORY_STRUCTURE
from ..tools.critic import critic_agent, approve_draft



genre_router_agent = Agent(
    name="genre_router_agent",
    model="gemini-3-pro-preview",
    instruction="""
You are a genre classification agent.

Your job is to analyze the user's prompt and determine which story genre is the best fit.

Available genres:

1. Sci-Fi
2. Fantasy
3. Romance
4. Adventure
5. Mystery
6. Thriller
7. Horror
8. Historical
9. Drama
10. Inspirational / Sports

Rules:
- Carefully understand the main theme of the prompt.
- Select the genre that best matches the story concept.
- Output ONLY the genre name.

Do not write the story.
Only output the selected genre.
"""
)


GENRE_AGENT_MAP = {
    "Sci-Fi": scifi_writer_agent,
    "Fantasy": fantasy_writer_agent,
    "Romance": romance_writer_agent,
    "Adventure": adventure_writer_agent,
    "Mystery": mystery_writer_agent,
    "Thriller": thriller_writer_agent,
    "Horror": horror_writer_agent,
    "Historical": historical_writer_agent,
    "Drama": drama_writer_agent,
    "Inspirational": inspirational_writer_agent
}

