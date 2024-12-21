from fastapi import FastAPI
from src.routing.routing_note import app as note_router
from src.routing.routing_service import app as service_router

app = FastAPI()

app.include_router(note_router)
app.include_router(service_router)
