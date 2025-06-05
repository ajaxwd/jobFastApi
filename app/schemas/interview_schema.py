from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class InterviewBase(BaseModel):
    user_id: int
    company_id: int
    scheduled_at: datetime
    location: Optional[str] = None
    notes: Optional[str] = None
    proposal_id: Optional[int] = None


class CreateInterviewDTO(InterviewBase):
    pass


class InterviewResponse(InterviewBase):
    id: int
    uid: UUID
    created_at: datetime

    class Config:
        from_attributes = True
