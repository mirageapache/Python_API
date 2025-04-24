"""
測試包
"""
import pytest
from fastapi.testclient import TestClient
from app import app

@pytest.fixture
def client():
    return TestClient(app)

__all__ = ["client"] 