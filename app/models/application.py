from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Application(Base):
    """
    Modelo que representa una aplicación a una publicación de trabajo.

    Cada aplicación está asociada a un usuario y una publicación.
    Las aplicaciones pueden tener diferentes estados (submitted, in_review, rejected, hired, etc.).
    Las aplicaciones se relacionan con el usuario a través de la clave foránea user_id.
    Las aplicaciones se relacionan con la publicación a través de la clave foránea posting_id.
    """
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(UUID(as_uuid=True), unique=True,
                 default=uuid.uuid4, nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    posting_id = Column(Integer, ForeignKey("postings.id"), nullable=False)

    cover_letter = Column(Text, nullable=True)
    # submitted, in_review, rejected, hired, etc.
    status = Column(String(50), default="submitted")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    user = relationship("User", backref="applications")
    posting = relationship("Posting", back_populates="applications")
