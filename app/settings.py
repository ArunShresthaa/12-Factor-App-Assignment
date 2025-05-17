from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    port: int = '4444'
    log_level: str = "info"
    redis_url: str = "None"

    class Config:
        env_file = ".env"


settings = Settings()
