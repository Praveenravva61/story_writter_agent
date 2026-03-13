from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ..tools.base_instruction import BASE_STORY_STRUCTURE
from ..tools.critic import critic_agent, approve_draft

#==============================================================
# LoopAgent:
#      ADK's LoopAgent wraps a sub-agent and run it repeatedly,
# up to max_iterations. To break out of this loop successfully before
# hitting the max, an agent can use tool call like this.

# setting "tool_context.actions.escilate=True" tells the adk runner 
# immediately stop the loop and return the current agent's response as the final answer.
#==============================================================




#==================================================================================================
# Sci-fi writer and critic agents:
#==================================================================================================

scifi_writer_agent = Agent(
    name="scifi_writer_agent",
    model="gemini-3-pro-preview",
    instruction=(
        BASE_STORY_STRUCTURE +
        """

Genre: Science Fiction

Additional Guidelines:
- The story should include futuristic technology, space, AI, or advanced science.
- The world should feel imaginative and believable.
- Use scientific or cosmic elements to create wonder and mystery.
- The climax should involve a major scientific or technological revelation.
"""
    ),
    output_key="latest_draft"
)

story_pipeline_agent = LoopAgent(
    name="story_pipeline_agent",
    sub_agents=[
        scifi_writer_agent,
        critic_agent
    ],
    max_iterations=4
)


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

greeting_agent= Agent(
    name= "greeting_agent",
    model= 'gemini-3-pro-preview',
    instruction= """
    Respond politely to the user greeting like:
    User: Hi there!
    Agent: Hello! How can I assist you today?
    
    you can more polite and professional than the example above.and also mention im 
    professional in writing sci-fi story writting.
""",
)
fantasy_story_pipeline = LoopAgent(
    name="fantasy_story_pipeline",
    sub_agents=[
        fantasy_writer_agent,
        critic_agent
    ],
    max_iterations=4
)
    
    
root_agent= LlmAgent(
    name= "router_agent",
    model= 'gemini-3-pro-preview',
    instruction= """
    You are a helpful assistant that routes the user's request to the appropriate agent.
    if user greats you, route to greeting_agent.
    if user ask for a story, route to story_loop_agent.""",
    sub_agents=[greeting_agent, stroy_loop_agent]
)


from google.adk.apps import App
app= App(
    name= "critic_agent",
    root_agent= root_agent
)

