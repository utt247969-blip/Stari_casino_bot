import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "8932934972:AAE7cmfNNSlQImWZYM9BF3ASRBdUV6md1_0")
    ADMIN_USERNAME: str = os.getenv("ADMIN_USERNAME", "ku13i")
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./casiubrot.db")

settings = Settings()