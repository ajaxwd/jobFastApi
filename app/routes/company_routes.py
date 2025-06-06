from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services import company_service
from app.db.session import get_db
from app.schemas.company_schema import CreateCompanyDTO, CompanyResponse
from typing import List

router = APIRouter()

# Crear empresa


@router.post("/", response_model=CompanyResponse)
def create_company(company: CreateCompanyDTO, db: Session = Depends(get_db)):
    return company_service.create_company(db, company)

# Listar empresas


@router.get("/", response_model=List[CompanyResponse])
def get_companies(db: Session = Depends(get_db)):
    return company_service.get_companies(db)
