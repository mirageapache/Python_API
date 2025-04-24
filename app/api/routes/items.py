from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.get("/")
async def read_items(db: AsyncSession = Depends(get_db)):
    return [{"name": "項目1", "price": 100}, {"name": "項目2", "price": 200}] 