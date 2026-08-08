from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "AI Document Assistant"
    VERSION: str = "2.0.0"
    API_PREFIX: str = "/api"

    GOOGLE_API_KEY: str

    class Config:
        env_file = ".env"


settings = Settings()