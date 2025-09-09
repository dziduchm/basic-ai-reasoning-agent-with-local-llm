from typing import Any
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from agents.retriever import RetrieverAgent
from agents.reasoner import ReasonerAgent
from agents.supervisor import SupervisorAgent
from models.state import AgentState
import logging
import yaml
import os

# Configure basic logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SettingsBuilder:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), '../../config/app_config.yaml')
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
    def get_llm_model(self):
        return self.config['llm_config']['model']
    def get_llm_base_url(self):
        return self.config['llm_config']['base_url']
    def get_chunk_size(self):
        return self.config['chunking']['default_size']
    def get_input_file(self):
        return self.config['input']['input_file']
    def get(self, section, key, default=None):
        return self.config.get(section, {}).get(key, default)

class Workflow:
    def __init__(self, settings=None):
        self.settings = settings or SettingsBuilder()
        self.graph = StateGraph(state_schema=AgentState)
        self.retriever = RetrieverAgent(self.settings)
        self.reasoner = ReasonerAgent(self.settings)
        self.supervisor = SupervisorAgent(self.settings)
        self._setup_graph()

    def _setup_graph(self):
        # Add nodes
        self.graph.add_node("retrieve", self.retriever.process)
        self.graph.add_node("reason", self.reasoner.process)
        self.graph.add_node("supervisor", self.supervisor.decide)

        # Add conditional edges based on 'next_step'
        def get_next_node(state: Any) -> str:
            logger.info(f"get_next_node received state: {state}")
            logger.info(f"get_next_node app nodes: {self.graph.nodes}")
            state_dict = state.dict() if hasattr(state, "dict") else dict(state) if isinstance(state, (dict, AgentState)) else {}
            next_step = state_dict.get("next_step")
            if next_step is None:
                # Default to 'retrieve' for the first step or if next_step is missing
                if not state_dict.get("chunks") and not state_dict.get("reasoning_steps"):
                    logger.info("Initial state detected, defaulting to 'retrieve'")
                    return "retrieve"
                logger.warning("No next_step found, defaulting to 'end'")
                return "end"
            valid_steps = {"retrieve", "reason", "end"}
            if next_step not in valid_steps:
                logger.warning(f"Invalid next_step value: {next_step}, defaulting to 'end'")
                return "end"
            logger.info(f"get_next_node returning: {next_step}")
            return next_step

        self.graph.add_conditional_edges(
            "supervisor",
            get_next_node,
            {
                "retrieve": "retrieve",
                "reason": "reason",
                "end": END
            }
        )
        self.graph.add_edge("retrieve", "supervisor")
        self.graph.add_edge("reason", "supervisor")
        self.graph.set_entry_point("supervisor")

        # Compile with memory
        self.memory = MemorySaver()
        self.app = self.graph.compile(checkpointer=self.memory)

    def run(self, initial_state):
        
        config = {"thread_id": "1"} 
        final_state = None
        for event in self.app.stream(initial_state, config):
            print(event)
            logger.info(f"Event in run: {event}")
            # Update final_state with the last event's state
            if "updates" in event and event["updates"]:
                final_state = event["updates"]
        # Get the final answer from the last state update. Note: final_state may be None if no updates occurred.
        return final_state.get("final_answer") if final_state else "No answer generated"

if __name__ == "__main__":
    workflow = Workflow()
    initial_state = {"query": "Based on the meeting notes, which team should receive the most resources, and why?", "chunks": [], "reasoning_steps": [], "final_answer": ""}
    final_answer = workflow.run(initial_state)
    print("Final Answer:", final_answer)