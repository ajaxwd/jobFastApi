import os


class Settings:
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecret")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(
        os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    REFRESH_TOKEN_EXPIRE_DAYS = int(
        os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", "7"))
    REFRESH_SECRET_KEY = os.getenv("REFRESH_SECRET_KEY", "supersecret")


settings = Settings()
