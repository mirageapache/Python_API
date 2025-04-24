from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# 創建異步引擎
engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True,  # 設置為 True 可以在控制台看到 SQL 語句
    future=True
)

# 創建異步會話工廠
AsyncSessionLocal = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 依賴注入函數
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close() 