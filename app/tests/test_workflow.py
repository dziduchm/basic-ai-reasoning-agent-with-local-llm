import pytest
from src.graph.workflow import Workflow, SettingsBuilder
from src.models.state import AgentState

def test_workflow_integration():
    settings = SettingsBuilder()
    workflow = Workflow(settings)
    initial_state = AgentState(
        query="What is the main topic in sample.txt?",
        chunks=[],
        reasoning_steps=[],
        final_answer=""
    )
    final_answer = workflow.run(initial_state)
    print("Integration Test Final Answer:", final_answer)
    assert isinstance(final_answer, str)
    assert final_answer != "No answer generated"
    assert "NLP" in final_answer or "chatbot" in final_answer or "AI" in final_answer


