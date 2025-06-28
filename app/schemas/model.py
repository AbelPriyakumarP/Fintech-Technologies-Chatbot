from pydantic import BaseModel
from typing import List

class QueryRequest(BaseModel):
    user_id: str
    query: str

class QueryResponse(BaseModel):
    response: str
    sources: List[str]