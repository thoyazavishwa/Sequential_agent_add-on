import os
from google.adk.agents import Agent
from typing import Dict, Any

# Import instruction from prompt file
from ...prompts.statrequestescalator_instruction import system_instruction

# Import tools
# from ...tools.default_tool import default_tool

def create_agent() -> Agent:
    """Create and configure the statrequestescalator agent."""
    return Agent(
        name="statrequestescalator_agent",
        model="gemini-2.0-flash",
        description="""Identifies and escalates urgent PA requests.""",
        instruction=system_instruction,
        tools=[]
    )

# Create the agent instance
statrequestescalator_agent = create_agent()
