from sqlalchemy import text
from app.db import engine

with engine.connect() as conn:
    conn.execute(text("SELECT 1"))
    print("Connected to Postgres successfully.")
