from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class ProposalBase(BaseModel):
    company_id: int
    user_id: int
    message: str = Field(
        ..., example="Estamos interesados en tu perfil para una posición de Data Scientist.")


class CreateProposalDTO(ProposalBase):
    pass


class UpdateProposalDTO(BaseModel):
    message: Optional[str]
    status: Optional[str]  # accepted, rejected, etc.


class ProposalResponse(ProposalBase):
    id: int
    uid: UUID
    status: str
    created_at: datetime

    class Config:
        from_attributes = True
