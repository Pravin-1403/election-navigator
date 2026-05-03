from pydantic import BaseModel, Field
from typing import Optional, List

class UserInfo(BaseModel):
    age: Optional[int] = Field(None, ge=1, le=120, description="Age of the user")
    state: Optional[str] = Field(None, max_length=50, description="State of residence")
    is_first_time_voter: Optional[bool] = Field(None, description="Whether the user is a first-time voter")
    language: Optional[str] = Field("English", max_length=20, description="Preferred response language")

class Message(BaseModel):
    role: str = Field(..., description="Role of the sender (user or model)")
    content: str = Field(..., description="Content of the message")

class ChatRequest(BaseModel):
    query: str = Field(..., min_length=1, max_length=1000, description="User's question about the election")
    user_info: Optional[UserInfo] = None
    history: Optional[List[Message]] = Field(default_factory=list, description="Previous chat history")

class ChatResponse(BaseModel):
    response: str
