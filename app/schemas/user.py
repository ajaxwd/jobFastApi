from pydantic import BaseModel, EmailStr
from typing import Optional


class UserBase(BaseModel):
    uid: Optional[str]
    name: str
    email: EmailStr
    photo_url: Optional[str] = None
    stack: Optional[str] = None
    experience: Optional[int] = None
    modality: Optional[str] = None
    availability: Optional[str] = None
    portfolio: Optional[str] = None
    is_open_to_offers: Optional[bool] = True


class UserCreate(UserBase):
    password: str


class UserOut(BaseModel):
    id: int
    uid: Optional[str]
    name: str
    email: EmailStr
    photo_url: Optional[str]
    stack: Optional[str]
    experience: Optional[int]
    modality: Optional[str]
    availability: Optional[str]
    portfolio: Optional[str]
    is_open_to_offers: Optional[bool]

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[EmailStr]
    photo_url: Optional[str]
    stack: Optional[str]
    experience: Optional[int]
    modality: Optional[str]
    availability: Optional[str]
    portfolio: Optional[str]
    is_open_to_offers: Optional[bool]


class LoginDTO(BaseModel):
    email: EmailStr
    password: str


class RefreshTokenDTO(BaseModel):
    refresh_token: str
