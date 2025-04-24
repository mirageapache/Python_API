from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db

router = APIRouter()

@router.get("/test-db-connection")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        # 執行一個簡單的查詢來測試連線
        result = await db.execute(text("SELECT 1"))
        return {"status": "success", "message": "資料庫連線成功"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"資料庫連線失敗: {str(e)}"
        ) 