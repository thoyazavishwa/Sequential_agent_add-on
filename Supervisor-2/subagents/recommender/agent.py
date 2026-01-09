import os
from google.adk.agents import Agent, LlmAgent
from typing import Dict, Any

# Import instruction from prompt file
from ...prompts.recommender_instruction import system_instruction

# Import tools
# from ...tools.default_tool import default_tool

def create_agent() -> LlmAgent:
    """Create and configure the recommender agent."""
    return LlmAgent(
        name="recommender_agent",
        model="gemini-2.0-flash",
        description="""Recommends next actions based on lead qualification.""",
        instruction=system_instruction,
        tools=[],
        output_key="action_recommendation"
    )

# Create the agent instance
recommender_agent = create_agent()
