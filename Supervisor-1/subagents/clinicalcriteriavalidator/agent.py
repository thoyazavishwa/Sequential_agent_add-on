import os
from google.adk.agents import Agent
from typing import Dict, Any

# Import instruction from prompt file
from ...prompts.clinicalcriteriavalidator_instruction import system_instruction

# Import tools
# from ...tools.default_tool import default_tool

def create_agent() -> Agent:
    """Create and configure the clinicalcriteriavalidator agent."""
    return Agent(
        name="clinicalcriteriavalidator_agent",
        model="gemini-2.0-flash",
        description="""Validates PA requests against clinical criteria.""",
        instruction=system_instruction,
        tools=[]
    )

# Create the agent instance
clinicalcriteriavalidator_agent = create_agent()
