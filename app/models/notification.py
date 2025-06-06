from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Notification(Base):
    """
    Modelo que representa una notificación en el sistema.

    Cada notificación está asociada a un usuario o una empresa y puede tener un enlace a una propuesta, entrevista, etc.
    Las notificaciones se relacionan con el usuario a través de la clave foránea user_id.
    Las notificaciones se relacionan con la empresa a través de la clave foránea company_id.
    """
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(UUID(as_uuid=True), unique=True,
                 default=uuid.uuid4, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=True)

    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    # puede ser un enlace a una propuesta, entrevista, etc.
    link = Column(String(512), nullable=True)
    read = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    user = relationship("User", backref="notifications")
    company = relationship("Company", backref="notifications")
