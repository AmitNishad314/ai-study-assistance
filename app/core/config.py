from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "AI Document Assistant"
    VERSION: str = "2.0.0"
    API_PREFIX: str = "/api"

    GOOGLE_API_KEY: str
    MODEL_NAME: str = "gemini-flash-latest"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

settings = Settings()