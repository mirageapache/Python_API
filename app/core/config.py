from pydantic_settings import BaseSettings
from typing import Optional
from pathlib import Path
from dotenv import load_dotenv

# 加載 .env 文件
env_path = Path(__file__).parent.parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

class Settings(BaseSettings):
    # 應用配置
    PROJECT_NAME: str = "FastAPI 應用"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # 數據庫配置
    DATABASE_URL: str
    
    # JWT 配置
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings() 