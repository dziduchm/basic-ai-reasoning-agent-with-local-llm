from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor

class SupervisorAgent:
    def __init__(self, settings=None):
        self.settings = settings
        llm_model = self.settings.get_llm_model() if self.settings else "llama3.1"
        llm_base_url = self.settings.get_llm_base_url() if self.settings else "http://host.docker.internal:11434"
        self.llm = ChatOllama(model=llm_model, base_url=llm_base_url)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a supervisor agent. Decide the next step: 'retrieve', 'reason', or 'end' based on the current state."),
            ("human", "State: {state}"),
            ("placeholder", "{agent_scratchpad}")  # For tool call history
        ])
        self.agent = create_tool_calling_agent(self.llm, [], self.prompt)
        self.executor = AgentExecutor(agent=self.agent, tools=[], verbose=True)

    def decide(self, state):
        result = self.executor.invoke({"state": str(state)})
        print()
        print(f"\nSupervisor decision result:{result}\n")
        print()
        decision = result.get("output", "").lower()  # 'retrieve', 'reason', or 'end'
        return {"next_step": decision}