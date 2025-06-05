from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
import uuid

from app.db.base import Base


class Posting(Base):
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
