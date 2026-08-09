from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.core.config import settings
from app.core.exceptions import (
    APIException,
    api_exception_handler
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
)
app.add_exception_handler(
    APIException,
    api_exception_handler
)

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)