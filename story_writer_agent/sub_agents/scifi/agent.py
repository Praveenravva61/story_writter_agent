from google.adk.agents import Agent,LoopAgent, LlmAgent
from google.adk.tools import FunctionTool,ToolContext
from ...tools.base_instruction import BASE_STORY_STRUCTURE
from ...tools.critic import critic_agent, approve_draft

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

scifi_pipeline_agent = LoopAgent(
    name="scifi_pipeline_agent",
    sub_agents=[
        scifi_writer_agent,
        critic_agent()
    ],
    max_iterations=4
)




