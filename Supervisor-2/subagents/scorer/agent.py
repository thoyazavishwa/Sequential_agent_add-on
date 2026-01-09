import os
from google.adk.agents import Agent,LlmAgent
from typing import Dict, Any

# Import instruction from prompt file
from ...prompts.scorer_instruction import system_instruction

# Import tools
# from ...tools.default_tool import default_tool

def create_agent() -> LlmAgent:
    """Create and configure the scorer agent."""
    return LlmAgent(
        name="scorer_agent",
        model="gemini-2.0-flash",
        description="""Scores qualified leads on a scale of 1-10.""",
        instruction=system_instruction,
        tools=[],
        output_key="lead_score"
    )

# Create the agent instance
scorer_agent = create_agent()
