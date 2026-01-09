
from google.adk.agents import Agent
import os
from pathlib import Path

# Import sub-agents
from .subagents.clinicalcriteriavalidator import clinicalcriteriavalidator_agent
from .subagents.statrequestescalator import statrequestescalator_agent

# Import instructions
from .prompts.system_instruction import system_instruction
from .prompts.final_response_instruction import system_instruction as final_response_instruction

# Combine instructions for supervisor agent
combined_instruction = f"""{system_instruction}

## Response Format Requirements
{final_response_instruction}"""

# List of sub-agents to be executed in parallel/hierarchical fashion
sub_agents_list = [clinicalcriteriavalidator_agent, statrequestescalator_agent]

# --- AGENT TYPE EXPLANATION ---
# This Supervisor agent uses Agent, which means:
#   - All sub-agents are executed independently and in parallel (no order, no dependency).
#   - Use Agent when you want multiple checks or actions on the same input, and results are combined or coordinated.
#   - Syntax difference: Agent requires 'model', 'instruction', and sub_agents (list, order does not matter).
#   - sub_agents argument can be any list (order is not important).
#   - Typical use: Multiple validators, escalators, or processors working on the same data.
#
# For sequential/pipeline execution, use SequentialAgent instead:
#   - SequentialAgent executes sub-agents in order, passing output from one to the next.
#   - Syntax: SequentialAgent does NOT require 'model' or 'instruction' in constructor, but you can add if needed.
#   - sub_agents argument must be ordered (order matters).
#
# Example for sequential agent (not used here):
# root_agent = SequentialAgent(
#     name="supervisor_agent",
#     description="Coordinates between specialized subagents",
#     sub_agents=sub_agents_list
# )
#
# To switch between normal and sequential agent, change the class and adjust sub_agents_list as needed.

root_agent = Agent(
    name="supervisor_agent",
    model="gemini-2.0-flash",
    description="Coordinates between specialized subagents",
    instruction=combined_instruction,
    sub_agents=sub_agents_list
)

# For backward compatibility
supervisor_agent = root_agent
