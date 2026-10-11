from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "AI Document Assistant"
    VERSION: str = "1.0.0"

    GEMINI_API_KEY: str

    MODEL_NAME: str = "gemini-flash-latest"

    CHROMA_API_KEY: str
    CHROMA_TENANT: str
    CHROMA_DATABASE: str

    SUPABASE_SERVICE_ROLE_KEY: str
    SUPABASE_URL: str

    UPLOAD_DIR: str = "storage/uploads"
    CHROMA_DIR: str = "storage/chroma_db"

    class Config:
        env_file = ".env"


settings = Settings()
print("MODEL =", settings.MODEL_NAME)