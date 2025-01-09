from fastapi import APIRouter, HTTPException

from src.repositories import with_database
from src.schemas import Note

app = APIRouter(
    prefix="/note",
    tags=["note📓"],
    )


@app.get("/notes_all")
async def get_all_notes():
    result = with_database.get_all_notes_db()
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result


@app.get("/{id}")
async def get_note_by_id(id: int):
    result = with_database.get_note_db_with_id(id=id)
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result


@app.get("/note_by_name")
async def get_note_by_name(name: str):
    result = with_database.get_note_db_with_name(name=name)
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result


@app.post("/create_note")
async def create_note(note: Note):
    result = with_database.create_new_note_db(note=note)
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result


@app.delete("/delete_note")
async def delete_note(id: int):
    result = with_database.delete_note_db_with_id(id=id)
    if not result["Connection"]:
        raise HTTPException(
            status_code=500,
            detail=result.get("Reply")
            )
    return result
