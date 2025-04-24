from fastapi import FastAPI
from pydantic import BaseModel
from app.core.config import settings
from app.api.api import api_router

# 創建 FastAPI 應用實例
app = FastAPI(
    title=settings.PROJECT_NAME,
    description="這是一個簡單的 API 示例",
    version=settings.VERSION
)

# 包含 API 路由
app.include_router(api_router, prefix=settings.API_V1_STR)

# 定義一個簡單的數據模型
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# 根路徑
@app.get("/")
async def root():
    return {"message": "歡迎使用 pyAPI！"}

# 獲取項目列表
@app.get("/items/")
async def read_items():
    return [
        {"name": "項目1", "price": 100},
        {"name": "項目2", "price": 200}
    ]

# 創建新項目
@app.post("/items/")
async def create_item(item: Item):
    return item

# 獲取特定項目
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"項目 {item_id}"} 