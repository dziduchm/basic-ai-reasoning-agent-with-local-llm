from langchain_core.tools import tool
import os

class FileTools:
    settings = None
    @staticmethod
    @tool
    def file_reader(file_path: str) -> str:
        """Read content from a local file in the documents directory."""
        if not file_path:
            file_path = FileTools.settings.get_input_file() if FileTools.settings else "/workspaces/ai-app/app/documents/sample.txt"
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error reading file: {str(e)}"