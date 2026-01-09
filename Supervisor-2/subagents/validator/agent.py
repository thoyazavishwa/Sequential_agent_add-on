import os
from google.adk.agents import Agent, LlmAgent
from typing import Dict, Any

# Import instruction from prompt file
from ...prompts.validator_instruction import system_instruction

# Import tools
# from ...tools.default_tool import default_tool

def create_agent() -> LlmAgent:
    """Create and configure the validator agent."""
    return LlmAgent(
        name="validator_agent",
        model="gemini-2.0-flash",
        description="""Validates lead information for completeness.""",
        instruction=system_instruction,
        tools=[],
        output_key="validation_status"
    )

# Create the agent instance
validator_agent = create_agent()
