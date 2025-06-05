import logging
from fastapi import APIRouter, Depends, Path, status, Request
from sqlalchemy.orm import Session
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.user import UserCreate, UserOut, UserUpdate, LoginDTO, RefreshTokenDTO
from app.services import user_service
from app.db.session import get_db
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import HTTPException
from sqlalchemy import text
from fastapi import Body

router = APIRouter()

# Login


@router.post("/login", tags=["Users"])
def login(login_data: LoginDTO, db: Session = Depends(get_db)):
    return user_service.login_user(login_data, db)

# Refresh token


@router.post("/refresh")
def refresh_token(dto: RefreshTokenDTO, db: Session = Depends(get_db)):
    return user_service.refresh_token(dto, db)

# Crear usuario


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

# Obtener usuario


@router.get("/", response_model=list[UserOut])
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)


# Obtener usuario actual

@router.get("/me", response_model=UserOut)
def get_me(current_user: User = Depends(get_current_user)):
    return current_user

# Obtener usuario por id o uid


@router.get("/{identifier}", response_model=UserOut)
def get_user(identifier: str, db: Session = Depends(get_db)):
    return user_service.get_user_by_id_or_uid(db, identifier)

# Actualizar user


@router.put("/{user_id}", response_model=UserOut)
def update_user(
    user_id: int = Path(..., gt=0),
    user_data: UserUpdate = Depends(),
    db: Session = Depends(get_db)
):
    return user_service.update_user(db, user_id, user_data)

# Eliminar user


@router.delete("/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return user_service.delete_user(user_id=user_id, db=db)
