from fastapi import APIRouter
from app.api.routes import db_test

api_router = APIRouter()

# 添加資料庫測試路由
api_router.include_router(db_test.router, tags=["database"]) 