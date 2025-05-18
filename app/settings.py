# this follows the configuration principle from 12 factor app which recommends storing config in the environment
# rather than hardcoding it in the code

from pydantic_settings import BaseSettings
from pathlib import Path


class Settings(BaseSettings):
    port: int = 4444
    log_level: str = "info"
    redis_url: str = "None"

    class Config:
        # use the .env file from root dir
        env_file = Path(__file__).parent.parent / ".env"


settings = Settings()
