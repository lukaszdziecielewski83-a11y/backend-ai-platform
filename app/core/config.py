from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Backend AI Platform"
    app_version: str = "1.0.0"
    environment: str = "development"


settings = Settings()
