from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class PostingBase(BaseModel):
    company_id: int
    title: str
    description: str
    location: Optional[str]
    remote: Optional[bool] = False
    employment_type: Optional[str] = "full_time"
    stack: Optional[str]
    salary_range: Optional[str]


class CreatePostingDTO(PostingBase):
    pass


class UpdatePostingDTO(BaseModel):
    title: Optional[str]
    description: Optional[str]
    location: Optional[str]
    remote: Optional[bool]
    employment_type: Optional[str]
    stack: Optional[str]
    salary_range: Optional[str]


class PostingResponse(PostingBase):
    id: int
    uid: UUID
    created_at: datetime

    class Config:
        from_attributes = True
