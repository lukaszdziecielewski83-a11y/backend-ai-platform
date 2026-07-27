from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Backend AI Platform"
    app_version: str = "1.0.0"
    environment: str = "development"

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "backend_ai_platform"
    database_user: str = "postgres"
    database_password: str = "password"


settings = Settings()
