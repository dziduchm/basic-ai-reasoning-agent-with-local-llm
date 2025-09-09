# API Reference

## Tools
- `FileTools.file_reader(file_path: str)`: Reads content from a file in `/app/documents/`.
- `TextTools.text_chunker(text: str, chunk_size: int)`: Splits text into chunks of specified size.

## Agents
- `RetrieverAgent`: Fetches and chunks relevant document parts.
- `ReasonerAgent`: Analyzes chunks and provides reasoning.
- `SupervisorAgent`: Decides the next step ('retrieve', 'reason', or 'end').

## Workflow
- `Workflow`: Manages the LangGraph structure and runs the agentic process.