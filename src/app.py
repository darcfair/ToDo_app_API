from fastapi import FastAPI
from src.routing.routing_note import app as note_router
from src.routing.routing_service import app as service_router
from src.repositories.with_database import create_table_note


app = FastAPI()

try:
    create_table_note()
    app.include_router(note_router)
    app.include_router(service_router)
except Exception as ex:
    print("Err", ex)
