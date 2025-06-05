from pydantic import BaseModel, EmailStr, HttpUrl, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class CompanyBase(BaseModel):
    name: str = Field(..., example="OpenAI")
    email: EmailStr = Field(..., example="contact@openai.com")
    website: Optional[HttpUrl] = Field(None, example="https://openai.com")
    description: Optional[str] = Field(None, example="We build AI systems.")


class CreateCompanyDTO(CompanyBase):
    pass


class UpdateCompanyDTO(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    website: Optional[HttpUrl]
    description: Optional[str]


class CompanyResponse(CompanyBase):
    id: int
    uid: UUID
    created_at: datetime

    class Config:
        from_attributes = True
