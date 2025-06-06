from app.schemas.proposal_schema import CreateProposalDTO, ProposalResponse
from sqlalchemy.orm import Session
from app.models.proposal import Proposal
from datetime import datetime
from app.models.user import User
from app.models.company import Company
from fastapi import HTTPException


# Crear propuesta
def create_proposal(db: Session, proposal: CreateProposalDTO):
    # Verificar si el usuario existe
    user = db.query(User).filter(User.id == proposal.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Verificar si la empresa existe
    company = db.query(Company).filter(
        Company.id == proposal.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    # Verificar si la propuesta ya existe
    existing_proposal = db.query(Proposal).filter(
        Proposal.user_id == proposal.user_id,
        Proposal.company_id == proposal.company_id
    ).first()
    if existing_proposal:
        raise HTTPException(status_code=400, detail="Propuesta ya existe")
    # Crear la propuesta
    new_proposal = Proposal(
        user_id=proposal.user_id,
        company_id=proposal.company_id,
        message=proposal.message,
        status="pending",
        created_at=datetime.now()
    )
    db.add(new_proposal)
    db.commit()
    db.refresh(new_proposal)
    return new_proposal

# Listar propuestas por usuario


def list_user_proposals(db: Session, user_id: int):
    # Verificar si el usuario existe
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Listar las propuestas del usuario
    proposals = db.query(Proposal).filter(Proposal.user_id == user_id).all()
    return proposals

# Listar propuestas por empresa


def list_company_proposals(db: Session, company_id: int):
    # Verificar si la empresa existe
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    # Listar las propuestas de la empresa
    proposals = db.query(Proposal).filter(
        Proposal.company_id == company_id).all()
    return proposals
