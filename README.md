# FastAPI

使用 FastAPI 框架建立的 API 伺服器 side project。

## 環境需求

- Python 3.11
- 虛擬環境 (venv)

## 設定虛擬環境

1. 建立虛擬環境：
```bash
py -3.11 -m venv venv
```

2. 啟動虛擬環境：
```bash
.\venv\Scripts\activate
```

3. 退出虛擬環境：
```bash
deactivate
```

## 安裝依賴

```bash
pip install -r requirements.txt
```

## 運行伺服器

```bash
uvicorn main:app --reload
```

## API 端點

- `GET /`: 根路徑，返回歡迎訊息
- `GET /items/`: 獲取所有項目列表
- `POST /items/`: 創建新項目
- `GET /items/{item_id}`: 獲取特定項目

## API 文檔

運行伺服器後，你可以訪問以下地址查看 API 文檔：

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 