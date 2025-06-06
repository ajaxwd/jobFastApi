from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.proposal_schema import CreateProposalDTO, ProposalResponse
from app.services import proposal_service
from app.db.session import get_db

router = APIRouter()

# Crear propuesta


@router.post("/", response_model=ProposalResponse)
def create_proposal(proposal: CreateProposalDTO, db: Session = Depends(get_db)):
    return proposal_service.create_proposal(db, proposal)

# Listar propuestas por usuario


@router.get("/user/{user_id}", response_model=List[ProposalResponse])
def list_user_proposals(user_id: int, db: Session = Depends(get_db)):
    return proposal_service.list_user_proposals(db, user_id)

# Listar propuestas por empresa


@router.get("/company/{company_id}", response_model=List[ProposalResponse])
def list_company_proposals(company_id: int, db: Session = Depends(get_db)):
    return proposal_service.list_company_proposals(db, company_id)
