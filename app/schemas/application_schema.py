from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class ApplicationBase(BaseModel):
    user_id: int
    job_id: int
    cover_letter: Optional[str] = None


class CreateApplicationDTO(ApplicationBase):
    pass


class UpdateApplicationDTO(BaseModel):
    status: Optional[str]
    cover_letter: Optional[str]


class ApplicationResponse(ApplicationBase):
    id: int
    uid: UUID
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
