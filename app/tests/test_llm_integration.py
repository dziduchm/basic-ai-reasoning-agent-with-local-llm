import pytest
from langchain_ollama import ChatOllama

def test_llm_prompt_response():
    """Test sending a prompt to the local LLM and retrieving the answer."""
    llm = ChatOllama(model="llama3.1", base_url="http://host.docker.internal:11434")
    prompt = "What is the capital of France?"
    response = llm.invoke(prompt)
    assert isinstance(response, str) or hasattr(response, 'content'), "Response should be a string or have 'content' attribute."
    # If response is an object with 'content', extract it
    if hasattr(response, 'content'):
        answer = response.content
    else:
        answer = response
    assert "Paris".lower() in answer.lower(), f"Expected 'Paris' in answer, got: {answer}"
