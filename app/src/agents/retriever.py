from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools.file_reader import FileTools
from tools.text_chunker import TextTools

class RetrieverAgent:
    def __init__(self, settings=None):
        self.settings = settings
        llm_model = self.settings.get_llm_model() if self.settings else "llama3.1"
        llm_base_url = self.settings.get_llm_base_url() if self.settings else "http://host.docker.internal:11434"
        self.chunk_size = self.settings.get_chunk_size() if self.settings else 500
        self.input_file = self.settings.get_input_file() if self.settings else "/workspaces/ai-app/app/documents/sample.txt"
        self.llm = ChatOllama(model=llm_model, base_url=llm_base_url)
        self.prompt = ChatPromptTemplate.from_messages([
            ("system", f"You are a retriever agent. Use the 'file_reader' tool to fetch content from '{self.input_file}' and the 'text_chunker' tool to split it into chunks based on the query. The query will specify a file path (e.g., '{self.input_file}')."),
            ("human", "Query: {query}"),
            ("placeholder", "{agent_scratchpad}")  # For tool call history
        ])
        self.agent = create_tool_calling_agent(self.llm, [FileTools.file_reader, TextTools.text_chunker], self.prompt)
        self.executor = AgentExecutor(agent=self.agent, tools=[FileTools.file_reader, TextTools.text_chunker], verbose=True)

    def process(self, state):
        file_path = self.input_file
        result = self.executor.invoke({"query": state.query, "file_path": file_path})
        state.chunks = TextTools.text_chunker.invoke({"text": result.get("output", ""), "chunk_size": self.chunk_size})
        return state