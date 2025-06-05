from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class ConversationBase(BaseModel):
    sender_id: int
    receiver_id: int
    message: str


class CreateConversationDTO(ConversationBase):
    pass


class ConversationResponse(ConversationBase):
    id: int
    uid: UUID
    created_at: datetime

    class Config:
        from_attributes = True
