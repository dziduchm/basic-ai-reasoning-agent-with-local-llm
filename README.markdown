# Basic AI Reasoning Agent with Local LLM

![GitHub License](https://img.shields.io/github/license/dziduchm/basic-ai-reasoning-agent-with-local-llm)
![GitHub Issues](https://img.shields.io/github/issues/dziduchm/basic-ai-reasoning-agent-with-local-llm)
![GitHub Last Commit](https://img.shields.io/github/last-commit/dziduchm/basic-ai-reasoning-agent-with-local-llm)
[![Open in Visual Studio Code](https://open.vscode.dev/badges/open-in-vscode.svg)](https://open.vscode.dev/dziduchm/basic-ai-reasoning-agent-with-local-llm)

Welcome to the **Basic AI Reasoning Agent with Local LLM**, a cutting-edge, locally-hosted document question-answering system built with LangGraph, LangChain, and Ollama. This project, developed by [mr_dzi](https://github.com/dziduchm), showcases a sophisticated multi-agent architecture that leverages the power of local large language models (LLMs) for offline AI reasoning. Perfect for developers, researchers, and AI enthusiasts, this repository offers a scalable, secure, and customizable solution for processing and querying documents without relying on external APIs.

## Overview

The Basic AI Reasoning Agent with Local LLM is designed to provide intelligent responses to natural language queries based on local document content. Powered by the state-of-the-art `@llama3.1` model via Ollama, it features a modular agent-based workflow managed by LangGraph. This system excels in offline environments, making it ideal for privacy-conscious applications or environments with limited internet access. Key highlights include:

- **Multi-Agent Architecture**: Comprising `RetrieverAgent`, `ReasonerAgent`, and `SupervisorAgent` for seamless task orchestration.
- **Local LLM Integration**: Utilizes Ollama for running `@llama3.1` locally, ensuring data privacy and control.
- **Extensible Design**: Easily adaptable for new agents, tools, or document types with a well-structured codebase.
- **Dev Container Support**: Seamlessly integrates with Docker and VS Code for a reproducible development environment.

## Features
- Process and chunk local documents (e.g., `sample.txt`) for querying.
- Perform step-by-step reasoning to derive answers from document content.
- Support for configurable settings via a YAML configuration file.
- Comprehensive testing suite to ensure reliability and accuracy.
- Optimized for Windows with Docker Desktop integration.

## Setup

To get started with this project, follow these steps:

1. **Install Docker Desktop on Windows**:
   - Download and install from [Docker Desktop](https://www.docker.com/products/docker-desktop).
   - Configure custom Docker image storage (e.g., `D:\docker\images`) in Docker Desktop > Settings > Resources > Advanced.

2. **Clone the Repository**:
   - Clone this repo to your local machine:
     ```bash
     git clone https://github.com/dziduchm/basic-ai-reasoning-agent-with-local-llm.git
     cd basic-ai-reasoning-agent-with-local-llm
     ```

3. **Open in VS Code with Dev Containers**:
   - Open the project in Visual Studio Code.
   - Use the Dev Containers extension to **Rebuild and Reopen in Container** (Ctrl+Shift+P > "Dev Containers: Rebuild and Reopen in Container").

4. **Configure and Run**:
   - In the Dev Container terminal:
     - Start Ollama locally on your host: `ollama serve` (outside the container).
     - Pull the LLM model: `ollama pull llama3.1` (on your host).
     - Install dependencies and run the app:
       ```bash
       poetry install --no-root
       poetry run python app/src/main.py
       ```

## Usage

- **Prepare Documents**: Place your documents in the `documents/` folder (e.g., create `sample.txt` with meeting notes or other text).
- **Query the System**: Run the app with a query via `app/src/main.py`. For example, use the default query:
  ```python
  initial_state = {"query": "Based on the meeting notes, which team should receive the most resources, and why?", "chunks": [], "reasoning_steps": [], "final_answer": ""}
  ```
- **Expected Output**: The system will process the document, reason through the content, and print a `final_answer` (e.g., "The chatbot team should receive the most resources because...").

## Development

This project is designed for extensibility and collaboration. Here’s how you can contribute:

- **Add Tests**: Enhance the test suite in `app/tests/` with unit and integration tests.
- **Extend Agents and Tools**: Customize `app/src/agents/` and `app/src/tools/` to support new functionalities (e.g., PDF parsing, custom reasoning logic).
- **Configuration**: Modify `app/config/app_config.yaml` to adjust LLM models, chunk sizes, or input files.

### Prerequisites
- **Python 3.11+**
- **Docker Desktop**
- **Ollama** (installed locally on your host)
- **Poetry** (for dependency management)

### Recommended VS Code Extensions
- `ms-python.python` (Python support)
- `ms-vscode-remote.remote-containers` (Dev Container support)
- `yzhang.markdown-all-in-one` (Markdown editing)
- `ClemensPeters.format-json` (JSON formatting)
- `GitHub.github-vscode-theme` (Theme customization)

## Architecture

### Overview
The Basic AI Reasoning Agent employs a LangGraph-orchestrated multi-agent workflow, leveraging local LLMs via Ollama for robust, offline document analysis.

### Components
- **Agents**:
  - `RetrieverAgent`: Fetches and chunks document content.
  - `ReasonerAgent`: Performs step-by-step reasoning to answer queries.
  - `SupervisorAgent`: Orchestrates the workflow, deciding the next step.
- **Tools**:
  - `FileTools.file_reader`: Reads local files.
  - `TextTools.text_chunker`: Splits text into manageable chunks.
- **Workflow**: A `Workflow` class manages the StateGraph, ensuring state persistence with `MemorySaver`.
- **State**: Defined by a Pydantic `AgentState` model, tracking `query`, `chunks`, `reasoning_steps`, and `final_answer`.

### Flow
1. The user provides a query via `initial_state`.
2. The `SupervisorAgent` decides the initial step (`retrieve`, `reason`, or `end`).
3. The `RetrieverAgent` fetches and chunks the document.
4. The `ReasonerAgent` synthesizes the answer.
5. The `SupervisorAgent` concludes the process or loops back.

## Contributing

We welcome contributions to enhance this project! Please follow these steps:

1. **Fork the Repository**: Create your own fork on GitHub.
2. **Create a Feature Branch**: Use a descriptive name (e.g., `feature/new-agent`).
3. **Commit Changes**: Write clear commit messages.
4. **Push and Submit a Pull Request**: Include details of your changes and pass existing tests.
5. **Code Standards**: Adhere to PEP 8 and include tests in `app/tests/`.

### Issues and Bugs
Report issues via the [GitHub Issues](https://github.com/dziduchm/basic-ai-reasoning-agent-with-local-llm/issues) page. Provide reproducible steps and logs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Built with assistance from xAI’s Grok, showcasing advanced AI development expertise.
- Inspired by the LangChain and LangGraph communities for their innovative tools.
- Thanks to the Ollama project for enabling local LLM deployment.

## Contact

For questions or collaboration, reach out to [mr_dzi](https://github.com/dziduchm) via GitHub or X.com [@MarcinDziduch](https://x.com/MarcinDziduch).

---