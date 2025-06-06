from sqlalchemy import Column, Integer, String, Boolean, Text
from app.db.base import Base


class User(Base):
    """
    Modelo que representa un usuario en el sistema.

    Cada usuario tiene un nombre, email, contraseña, foto, stack, experiencia, modalidad, disponibilidad, portfolio y si está abierto a ofertas.
    Las aplicaciones se relacionan con el usuario a través de la clave foránea user_id.
    Las aplicaciones se relacionan con la publicación a través de la clave foránea posting_id.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    photo_url = Column(Text)
    stack = Column(Text)  # Comma-separated stack
    experience = Column(Integer)
    modality = Column(String)
    availability = Column(String)
    portfolio = Column(String)
    is_open_to_offers = Column(Boolean, default=True)
