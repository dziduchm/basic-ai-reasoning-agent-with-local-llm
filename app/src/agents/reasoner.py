from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

class ReasonerAgent:
    def __init__(self, settings=None):
        self.settings = settings
        llm_model = self.settings.get_llm_model() if self.settings else "llama3.1"
        llm_base_url = self.settings.get_llm_base_url() if self.settings else "http://host.docker.internal:11434"
        self.llm = ChatOllama(model=llm_model, base_url=llm_base_url)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a reasoner agent. Analyze the provided document chunks and provide step-by-step reasoning to answer the query."),
            ("human", "Query: {query}\nChunks: {chunks}"),
            ("placeholder", "{agent_scratchpad}")  # Added for tool call history
        ])
        self.agent = create_tool_calling_agent(self.llm, [], self.prompt)
        self.executor = AgentExecutor(agent=self.agent, tools=[], verbose=True)

    def process(self, state):
        result = self.executor.invoke({"query": state.query, "chunks": "\n".join(state.chunks)})
        state.reasoning_steps.append(result.get("output", ""))
        return state