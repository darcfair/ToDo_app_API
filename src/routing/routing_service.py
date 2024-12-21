from fastapi import APIRouter, HTTPException
from src.repositories import with_database

app = APIRouter(
    prefix="/service",
    tags=["service⚙️"],
    )


@app.get("/db_version", summary="Get data-base version")
async def get_version():
    result = with_database.get_version_db()
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result
