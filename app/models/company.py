from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Company(Base):
    """
    Modelo que representa una empresa en el sistema.

    Cada empresa tiene un nombre, email, sitio web, descripción y fecha de creación.
    Las empresas se relacionan con las publicaciones de trabajo a través de la clave foránea company_id.
    """
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(UUID(as_uuid=True), unique=True,
                 default=uuid.uuid4, nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    website = Column(String(150), nullable=True)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
