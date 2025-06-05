from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from datetime import datetime


class NotificationBase(BaseModel):
    title: str
    message: str
    link: Optional[str] = None
    user_id: Optional[int] = None
    company_id: Optional[int] = None


class CreateNotificationDTO(NotificationBase):
    pass


class NotificationResponse(NotificationBase):
    id: int
    uid: UUID
    read: bool
    created_at: datetime

    class Config:
        from_attributes = True
