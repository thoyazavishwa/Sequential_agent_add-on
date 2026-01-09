
from google.adk.agents import Agent, SequentialAgent
import os
from pathlib import Path

# Import sub-agents
from .subagents.recommender import recommender_agent
from .subagents.scorer import scorer_agent
from .subagents.validator import validator_agent

# Import instructions
from .prompts.system_instruction import system_instruction
from .prompts.final_response_instruction import system_instruction as final_response_instruction

# Combine instructions for supervisor agent
combined_instruction = f"""{system_instruction}

## Response Format Requirements
{final_response_instruction}"""

# List of sub-agents to be executed in sequence
sub_agents_list = [validator_agent, scorer_agent, recommender_agent]

# --- AGENT TYPE EXPLANATION ---
# This Supervisor agent uses SequentialAgent, which means:
#   - Each sub-agent is called one after another, passing output from one to the next (pipeline).
#   - Use SequentialAgent when you need strict ordering, dependency, or stepwise logic between agents.
#   - Syntax difference: SequentialAgent does NOT require 'model' or 'instruction' in constructor, but you can add if needed.
#   - sub_agents argument must be an ordered list (order matters).
#   - Typical use: Data validation -> scoring -> recommendation, where each step depends on previous.
#
# For parallel/hierarchical execution, use Agent instead:
#   - Agent executes all sub-agents independently (no order, no dependency).
#   - Syntax: Agent requires 'model', 'instruction', and sub_agents (list, order does not matter).
#   - Typical use: Multiple checks or actions on the same input, results are combined or coordinated.
#
# Example for parallel/hierarchical agent (not used here):
# root_agent = Agent(
#     name="supervisor_agent",
#     model="gemini-2.0-flash",
#     description="Coordinates between specialized subagents",
#     instruction=combined_instruction,
#     sub_agents=[general_agent, sequential_agent]
# )
#
# To switch between sequential and normal agent, change the class and adjust sub_agents_list as needed.

root_agent = SequentialAgent(
    name="supervisor_agent",
    description="Coordinates between specialized subagents",
    sub_agents=sub_agents_list
)

# For backward compatibility
supervisor_agent = root_agent
