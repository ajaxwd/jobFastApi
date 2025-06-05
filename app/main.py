from fastapi import FastAPI
from app.routes import notification_routes, user_routes
from app.db.session import engine
from app.db.base import Base

from app.models import *

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Reverse Job Board API")

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(notification_routes.router,
                   prefix="/notifications", tags=["Notifications"])
