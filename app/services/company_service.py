from app.schemas.company_schema import CreateCompanyDTO, CompanyResponse
from app.db.session import get_db
from sqlalchemy.orm import Session
from app.models.company import Company
from fastapi import HTTPException, status
from typing import List, Optional
import uuid

# Crear empresa


def create_company(db: Session, company: CreateCompanyDTO) -> Company:
    """
    Crea una nueva empresa en la base de datos.

    Args:
        db: Sesión de base de datos
        company: Datos de la empresa a crear

    Returns:
        Company: La empresa creada

    Raises:
        HTTPException: Si el email ya está registrado
    """
    # Verificar si el email ya existe
    existing_company = db.query(Company).filter(
        Company.email == company.email).first()
    if existing_company:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado"
        )

    # Convertir HttpUrl a string si existe
    website = str(company.website) if company.website else None

    # Crear nueva empresa
    new_company = Company(
        name=company.name,
        email=company.email,
        website=website,
        description=company.description
    )

    try:
        db.add(new_company)
        db.commit()
        db.refresh(new_company)
        return new_company
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al crear la empresa: {str(e)}"
        )

# Listar empresas


def get_companies(
    db: Session,
    skip: int = 0,
    limit: int = 100,
    search: Optional[str] = None
) -> List[Company]:
    """
    Obtiene la lista de empresas con opciones de paginación y búsqueda.

    Args:
        db: Sesión de base de datos
        skip: Número de registros a saltar
        limit: Límite de registros a retornar
        search: Término de búsqueda opcional

    Returns:
        List[Company]: Lista de empresas
    """
    query = db.query(Company)

    if search:
        search_term = f"%{search}%"
        query = query.filter(
            (Company.name.ilike(search_term)) |
            (Company.email.ilike(search_term)) |
            (Company.description.ilike(search_term))
        )

    return query.offset(skip).limit(limit).all()


def get_company_by_id(db: Session, company_id: int) -> Company:
    """
    Obtiene una empresa por su ID.

    Args:
        db: Sesión de base de datos
        company_id: ID de la empresa

    Returns:
        Company: La empresa encontrada

    Raises:
        HTTPException: Si la empresa no existe
    """
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa no encontrada"
        )
    return company


def get_company_by_uid(db: Session, company_uid: uuid.UUID) -> Company:
    """
    Obtiene una empresa por su UID.

    Args:
        db: Sesión de base de datos
        company_uid: UID de la empresa

    Returns:
        Company: La empresa encontrada

    Raises:
        HTTPException: Si la empresa no existe
    """
    company = db.query(Company).filter(Company.uid == company_uid).first()
    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Empresa no encontrada"
        )
    return company


def update_company(
    db: Session,
    company_id: int,
    company_data: CreateCompanyDTO
) -> Company:
    """
    Actualiza una empresa existente.

    Args:
        db: Sesión de base de datos
        company_id: ID de la empresa a actualizar
        company_data: Nuevos datos de la empresa

    Returns:
        Company: La empresa actualizada

    Raises:
        HTTPException: Si la empresa no existe o el email ya está en uso
    """
    company = get_company_by_id(db, company_id)

    # Verificar si el nuevo email ya está en uso por otra empresa
    if company_data.email != company.email:
        existing_company = db.query(Company).filter(
            Company.email == company_data.email,
            Company.id != company_id
        ).first()
        if existing_company:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El email ya está registrado por otra empresa"
            )

    # Actualizar campos
    for field, value in company_data.dict(exclude_unset=True).items():
        setattr(company, field, value)

    try:
        db.commit()
        db.refresh(company)
        return company
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar la empresa: {str(e)}"
        )


def delete_company(db: Session, company_id: int) -> dict:
    """
    Elimina una empresa.

    Args:
        db: Sesión de base de datos
        company_id: ID de la empresa a eliminar

    Returns:
        dict: Mensaje de confirmación

    Raises:
        HTTPException: Si la empresa no existe
    """
    company = get_company_by_id(db, company_id)

    try:
        db.delete(company)
        db.commit()
        return {"message": f"Empresa {company.name} eliminada correctamente"}
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar la empresa: {str(e)}"
        )
