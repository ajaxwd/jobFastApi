from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Posting(Base):
    """
    Modelo que representa una publicación de trabajo en el sistema.
    Cada publicación está asociada a una empresa y puede tener varias aplicaciones.
    Las aplicaciones se relacionan con la publicación a través de la clave foránea posting_id.
    Las aplicaciones pueden tener diferentes estados (submitted, in_review, rejected, hired, etc.).
    Las aplicaciones se relacionan con el usuario a través de la clave foránea user_id.
    Las aplicaciones se relacionan con la publicación a través de la clave foránea posting_id.
    Las aplicaciones se relacionan con el usuario a través de la clave foránea user_id.

    Attributes:
        id (int): Identificador único de la publicación
        uid (UUID): Identificador único universal de la publicación
        company_id (int): ID de la empresa que publica el trabajo
        title (str): Título del trabajo
        description (str): Descripción detallada del trabajo
        location (str): Ubicación del trabajo
        remote (bool): Indica si el trabajo es remoto
        employment_type (str): Tipo de empleo (full_time, part_time, etc.)
        stack (str): Tecnologías requeridas
        salary_range (str): Rango salarial ofrecido
        created_at (datetime): Fecha de creación de la publicación

    Relationships:
        company: Relación con la empresa que publica
        applications: Relación con las aplicaciones recibidas
    """
    __tablename__ = "postings"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(UUID(as_uuid=True), unique=True,
                 default=uuid.uuid4, nullable=False)

    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    location = Column(String(255), nullable=True)
    remote = Column(Boolean, default=False)
    # full_time, part_time, contract, freelance, etc.
    employment_type = Column(String(50), default="full_time")
    # Ej: "Python, FastAPI, PostgreSQL"
    stack = Column(String(255), nullable=True)
    # Ej: "$3000 - $4000 USD"
    salary_range = Column(String(100), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    company = relationship("Company", backref="postings")
    applications = relationship(
        "Application", back_populates="posting", cascade="all, delete")
