from pydantic_settings import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):

    
    DATABASE_URL: str
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    PROJECT_NAME: str = "AI Automation System"

    EMAIL_ADDRESS: str
    EMAIL_PASSWORD: str

    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_CHAT_ID: str

    GOOGLE_SHEET_NAME: str
    GOOGLE_CREDENTIALS_FILE: str
    
    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()