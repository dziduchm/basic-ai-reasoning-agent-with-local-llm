from langchain_core.tools import tool

class TextTools:
    settings = None

    @staticmethod
    @tool
    def text_chunker(text: str, chunk_size: int = 500) -> list:
        """Split text into chunks of specified size."""
        if TextTools.settings:
            chunk_size = TextTools.settings.get_chunk_size()
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]