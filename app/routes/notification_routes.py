from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.notification_schema import CreateNotificationDTO, NotificationResponse
from app.services import notification_service
from app.db.session import get_db

router = APIRouter()


@router.post("/", response_model=NotificationResponse)
def create_notification(notification: CreateNotificationDTO, db: Session = Depends(get_db)):
    return notification_service.create_notification(db, notification)


@router.get("/user/{user_id}", response_model=List[NotificationResponse])
def list_user_notifications(user_id: int, db: Session = Depends(get_db)):
    return notification_service.get_notifications_by_user(db, user_id)


@router.get("/company/{company_id}", response_model=List[NotificationResponse])
def list_company_notifications(company_id: int, db: Session = Depends(get_db)):
    return notification_service.get_notifications_by_company(db, company_id)


@router.put("/{notification_id}/read", response_model=NotificationResponse)
def mark_as_read(notification_id: int, db: Session = Depends(get_db)):
    return notification_service.mark_notification_as_read(db, notification_id)
