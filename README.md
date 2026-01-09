# AgentBuilder Project Workflows & UI Suggestions

This document compares the two agent project workflows in AgentBuilder and provides actionable UI suggestions for creating and managing agents.

---

## Project Overview

### 1. Project: Supervisor-1
- **Supervisor Agent:** Prior Authorization AI Coordinator
- **Subagents:**
  1. clinicalcriteriavalidator
  2. statrequestescalator
- **Workflow Type:** Normal Agent (Parallel/Hierarchical)

### 2. Project: Supervisor-2
- **Supervisor Agent:** Custom Agents
- **Subagents:**
  1. recommender_agent
  2. scorer_agent
  3. validator_agent
- **Workflow Type:** Sequential Agent (Pipeline)

---

## Workflow Comparison: Normal Agent vs Sequential Agent

### Normal Agent (Parallel/Hierarchical)
- Uses the `Agent` class.
- Subagents are executed in parallel or as a group; each receives the same input independently.
- Syntax:
  ```python
  root_agent = Agent(
      name="supervisor_agent",
      model="gemini-2.0-flash",
      instruction=combined_instruction,
      sub_agents=[clinicalcriteriavalidator_agent, statrequestescalator_agent]
  )
  ```
- **Use Case:** Multiple checks or actions on the same data (e.g., validation and escalation).
- **Order:** The order of subagents does not affect execution.
- **Subagent Type:** Typically uses `Agent` or `LlmAgent` for flexibility.

### Sequential Agent (Pipeline)
- Uses the `SequentialAgent` class.
- Subagents are executed one after another, passing output from one to the next (strict order).
- Syntax:
  ```python
  root_agent = SequentialAgent(
      name="supervisor_agent",
      description="Coordinates between specialized subagents",
      sub_agents=[validator_agent, scorer_agent, recommender_agent]
  )
  ```
- **Use Case:** Stepwise logic where each agent depends on the previous (e.g., validation → scoring → recommendation).
- **Order:** The order of subagents is critical; workflow follows the list order (not stack/FILO).
- **Subagent Type:** Use `LlmAgent` for flexible parameters like `output_key` to share state among subagents.
- **Note:** Remove `model` and `instruction` from `SequentialAgent` as they are not required.

### Stack/FILO Note
- When adding subagents in the UI, ensure the workflow order matches the intended pipeline (not reversed).
- UI should visually represent the order and allow reordering.

### Shared State
- Prefer `LlmAgent` for subagents to utilize `output_key` for passing shared state/results between agents.

### Hybrid Supervisor Agent
- You can create a root supervisor agent that can invoke subagents or groups of subagents (sequential, parallel, looped) as needed:
  ```python
  root_agent = Agent(
      name="supervisor_agent",
      model="gemini-2.0-flash",
      description="Coordinates between specialized subagents",
      instruction=combined_instruction,
      sub_agents=[general_agent, sequential_agent]
  )
  ```
- This allows flexible orchestration, combining different agent types.

---

## UI Suggestions for Agent Creation & Management

### After Creating Supervisor Agent
- User should be able to add **four types of worker agents**:
  1. **Parallel Agent**: Executes subagents in parallel (normal Agent).
  2. **Sequential Agent**: Executes subagents in strict order (SequentialAgent).
  3. **Looped Agent**: Repeats subagent(s) until a condition is met (e.g., success, N times).
  4. **Single Agent**: A standalone agent for simple tasks.

### UI Features
- **Agent Type Selection:**
  - Dropdown/toggle to select agent type (Parallel, Sequential, Looped, Single).
- **Subagent Ordering:**
  - For sequential agents, allow drag-and-drop or numbered list to set order.
- **Loop Configuration:**
  - For looped agents, allow user to specify loop conditions (e.g., until success, max iterations).
- **Visual Workflow:**
  - Show a clear visual representation of agent workflow (pipeline for sequential, branches for parallel, loop icon for looped).
- **Shared State:**
  - For sequential/looped agents, show how state/output is passed between agents.
- **Tooltips/Help:**
  - Add help text explaining each agent type and workflow.
- **Hybrid Orchestration:**
  - Allow supervisor agent to combine different types of worker agents for advanced workflows.

### Additional Recommendations
- Ensure the backend supports all agent types and passes correct parameters.
- Validate agent configuration before saving (e.g., check for required fields, correct order).
- Allow editing and reordering of subagents after creation.
- Provide workflow templates for common use cases (e.g., validation pipeline, escalation flow).

---

## Summary Table
| Agent Type      | Class             | Execution Order | Use Case                        | UI Feature                |
|-----------------|------------------|-----------------|----------------------------------|---------------------------|
| Parallel        | Agent            | Any             | Multiple checks/actions          | Branch view, add/remove   |
| Sequential      | SequentialAgent  | Ordered         | Stepwise pipeline                | Pipeline view, reorder    |
| Looped          | (Custom/Looped)  | Repeated        | Retry, repeat until condition    | Loop config, max tries    |
| Single          | Agent/LlmAgent   | Single          | Simple, atomic task              | Single agent card         |

---

*For further details, see comments in each project's `Supervisor/agent.py` file and subagent implementations.*





