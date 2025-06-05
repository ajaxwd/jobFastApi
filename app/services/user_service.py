import uuid
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate, LoginDTO, RefreshTokenDTO
from fastapi import HTTPException, status
from app.utils.security import verify_password, hash_password
from app.utils.jwt import create_access_token, create_refresh_token
import logging
from app.core.config import settings
from jose import JWTError, jwt

# Configurar logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Login


def login_user(login_data: LoginDTO, db: Session):
    logger.debug(f"Attempting login for email: {login_data.email}")
    user = db.query(User).filter(User.email == login_data.email).first()

    if not user:
        logger.error(f"No user found with email: {login_data.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(login_data.password, user.hashed_password):
        logger.error(f"Invalid password for user: {login_data.email}")
        raise HTTPException(status_code=401, detail="Invalid credentials")

    logger.debug(f"User found with ID: {user.id}")
    token_data = {"sub": str(user.id), "email": user.email}
    logger.debug(f"Creating token with data: {token_data}")

    access_token = create_access_token(token_data)
    refresh_token = create_refresh_token(token_data)
    logger.debug(f"Generated access token: {access_token}")
    logger.debug(f"Generated refresh token: {refresh_token}")

    return {"access_token": access_token, "refresh_token": refresh_token, "token_type": "bearer"}

# Refresh Token


def refresh_token(dto: RefreshTokenDTO, db: Session):
    try:
        payload = jwt.decode(dto.refresh_token, settings.REFRESH_SECRET_KEY, algorithms=[
                             settings.ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")

        user = db.query(User).filter(User.id == int(user_id)).first()
        if not user:
            raise HTTPException(
                status_code=404, detail="Usuario no encontrado")

        new_access_token = create_access_token(
            {"sub": str(user.id), "email": user.email})
        return {"access_token": new_access_token, "token_type": "bearer"}

    except JWTError:
        raise HTTPException(
            status_code=401, detail="Token inválido o expirado")

# Crear usuario


def create_user(db: Session, user: UserCreate):
    # Check if email already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="El email ya está registrado")

    # Generate a unique UID
    while True:
        new_uid = str(uuid.uuid4())
        # Check if UID already exists (very unlikely but good practice)
        if not db.query(User).filter(User.uid == new_uid).first():
            break

    # Create user with the new UID
    user_data = user.model_dump(exclude={"password"})
    user_data["uid"] = new_uid

    hashed_pw = hash_password(user.password)
    db_user = User(**user_data, hashed_password=hashed_pw)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Obtener usuario


def get_users(db: Session):
    return db.query(User).all()

# Obtener usuario por id o uid


def get_user_by_id_or_uid(db: Session, identifier: str) -> User:
    """Retrieve a user by either their ID or their uid."""
    query = db.query(User)
    if identifier.isdigit():
        query = query.filter(User.id == int(identifier))
    else:
        query = query.filter(User.uid == identifier)
    user = query.first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Actualizar usuario


def update_user(db: Session, user_id: int, user_data: UserUpdate) -> User:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    for field, value in user_data.dict(exclude_unset=True).items():
        setattr(user, field, value)

    db.commit()
    db.refresh(user)
    return user

# Eliminar usuario


def delete_user(user_id: int, db: Session):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")

    db.delete(user)
    db.commit()
    return {"message": f"Usuario con ID {user_id} eliminado correctamente"}
