"""
API 路由包
"""
from fastapi import APIRouter
from .routes import items

api_router = APIRouter()
api_router.include_router(items.router, prefix="/items", tags=["items"])

__all__ = ["api_router"] 