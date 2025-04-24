"""
數據模型包
"""
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

__all__ = ["Base"] 