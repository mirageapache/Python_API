"""
FastAPI 應用主包
"""
from fastapi import FastAPI
from .core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="FastAPI 應用程式"
)

__version__ = "1.0.0" 