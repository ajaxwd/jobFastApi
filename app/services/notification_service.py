from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.notification import Notification
from app.schemas.notification_schema import CreateNotificationDTO


def create_notification(db: Session, notification: CreateNotificationDTO):
    db_notification = Notification(**notification.model_dump())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def get_notifications_by_user(db: Session, user_id: int):
    return db.query(Notification).filter(Notification.user_id == user_id).order_by(Notification.created_at.desc()).all()


def get_notifications_by_company(db: Session, company_id: int):
    return db.query(Notification).filter(Notification.company_id == company_id).order_by(Notification.created_at.desc()).all()


def mark_notification_as_read(db: Session, notification_id: int):
    notification = db.query(Notification).filter(
        Notification.id == notification_id).first()
    if not notification:
        raise HTTPException(
            status_code=404, detail="Notificación no encontrada")
    notification.read = True
    db.commit()
    db.refresh(notification)
    return notification
