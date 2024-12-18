from fastapi import FastAPI, HTTPException
import with_database
import uvicorn

app = FastAPI()


@app.get("/version")
async def get_version():
    result = with_database.get_version_db()
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result


@app.get("/note/all")
async def get_all_notes():
    result = with_database.get_all_notes_db()
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
