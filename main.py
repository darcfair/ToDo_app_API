from fastapi import FastAPI
from with_database import get_version
import uvicorn

app = FastAPI()


@app.get("/version")
async def get_version_db():
    return get_version()


if __name__ == "__main__":
    uvicorn.run("main:app")
