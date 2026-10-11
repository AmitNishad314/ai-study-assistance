from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings
from app.core.exceptions import (
    APIException,
    api_exception_handler
)
from app.core.logging import logger

fastapi_app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)
logger.info("Application started.")
fastapi_app.add_exception_handler(
    APIException,
    api_exception_handler
)

fastapi_app.include_router(router)

# Wrap the whole application so CORS headers are also present on error responses.
app = CORSMiddleware(
    app=fastapi_app,
    allow_origins=[
        "http://localhost:5173",
        "https://ai-study-assistance-gules.vercel.app",
    ],
    allow_origin_regex=r"https://ai-study-assistance-[a-z0-9-]+-amit-8cbc\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)