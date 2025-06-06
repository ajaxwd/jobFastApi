from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.notification import Notification
from app.schemas.notification_schema import CreateNotificationDTO
from app.models.user import User
from app.models.company import Company


def create_notification(db: Session, notification: CreateNotificationDTO):
    # Verificar si el usuario existe
    user = db.query(User).filter(User.id == notification.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Verificar si la empresa existe
    company = db.query(Company).filter(
        Company.id == notification.company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    db_notification = Notification(**notification.model_dump())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


def get_notifications_by_user(db: Session, user_id: int):
    # Verificar si el usuario existe
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    # Listar las notificaciones del usuario
    return db.query(Notification).filter(Notification.user_id == user_id).order_by(Notification.created_at.desc()).all()


def get_notifications_by_company(db: Session, company_id: int):
    # Verificar si la empresa existe
    company = db.query(Company).filter(Company.id == company_id).first()
    if not company:
        raise HTTPException(status_code=404, detail="Empresa no encontrada")
    # Listar las notificaciones de la empresa
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
