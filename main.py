
from fastapi import FastAPI, Depends, HTTPException
from typing import Annotated
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db

app = FastAPI()


@app.get("/healthchecker")
async def healthchecker(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(text("SELECT 1"))
        result = result.fetchone()
        if result is None:
            raise HTTPException(
                status_code=500, detail="Database is not configured correctly"
            )
        return {"message": "Database configured correctly"}
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="Error connecting to the database")


@app.get("/")
async def index():
    return {"message": "Welcome to Contacts app!"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
