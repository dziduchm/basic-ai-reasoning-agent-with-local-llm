import pytest
from src.tools.file_reader import FileTools
from src.tools.text_chunker import TextTools

def test_file_reader():
    result = FileTools.file_reader.invoke({"file_path": "documents/sample.txt"})
    assert isinstance(result, str), "File reader should return a string"
    assert result.strip() != "", "File reader should return non-empty content for sample.txt"
    # Add more assertions based on expected content

def test_text_chunker():
    text = "This is a test text for chunking." * 10
    chunks = TextTools.text_chunker.invoke({"text": text, "chunk_size": 20})
    assert isinstance(chunks, list), "Text chunker should return a list"
    assert len(chunks) > 1, "Text should be split into multiple chunks"
    assert all(isinstance(c, str) for c in chunks), "All chunks should be strings"
    assert all(len(c) <= 20 for c in chunks), "Chunks should not exceed size limit"