from typing import List, Optional, Dict
from pydantic import BaseModel

class AgentState(BaseModel):
    query: str
    chunks: List[str]
    reasoning_steps: List[str]
    final_answer: str
    metadata: Optional[Dict[str, str]] = None