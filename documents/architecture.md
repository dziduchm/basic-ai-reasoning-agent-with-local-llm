# Architecture

## Overview
The Local QA Agentic App uses LangGraph to orchestrate a multi-agent workflow with local LLMs via Ollama.

## Components
- **Agents**: `RetrieverAgent`, `ReasonerAgent`, and `SupervisorAgent`, each powered by Ollama's Llama2 model.
- **Tools**: `FileTools` and `TextTools` for document processing, encapsulated as static methods.
- **Workflow**: A `Workflow` class managing the StateGraph with nodes for each agent and conditional edges for routing.
- **State**: Managed via a Pydantic `AgentState` model with memory checkpoints.

## Flow
1. User provides a query.
2. `SupervisorAgent` decides the next step.
3. `RetrieverAgent` fetches and chunks documents.
4. `ReasonerAgent` synthesizes answers.
5. `SupervisorAgent` ends the process or loops back.