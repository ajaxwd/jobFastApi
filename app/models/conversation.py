from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Conversation(Base):
    """
    Modelo que representa una conversación entre dos usuarios.

    Cada conversación está asociada a dos usuarios y puede tener varios mensajes.
    Las conversaciones se relacionan con los usuarios a través de las claves foráneas sender_id y receiver_id.
    """
    __tablename__ = "conversations"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(UUID(as_uuid=True), unique=True,
                 default=uuid.uuid4, nullable=False)

    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    message = Column(Text, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relaciones
    sender = relationship("User", foreign_keys=[
                          sender_id], backref="sent_conversations")
    receiver = relationship("User", foreign_keys=[
                            receiver_id], backref="received_conversations")
