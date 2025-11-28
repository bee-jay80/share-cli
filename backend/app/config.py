from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "SwiftShare Backend"
    APP_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"

settings = Settings()