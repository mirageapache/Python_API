import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database():
    # 連接到 postgres 數據庫
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )
    
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    # 創建游標
    cur = conn.cursor()
    
    try:
        # 創建數據庫
        cur.execute("CREATE DATABASE fastapi_db")
        print("數據庫創建成功！")
    except psycopg2.Error as e:
        print(f"創建數據庫時出錯：{e}")
    finally:
        # 關閉游標和連接
        cur.close()
        conn.close()

if __name__ == "__main__":
    create_database() 