from pydantic import BaseModel, Field


class Note(BaseModel):
    name: str = Field(max_length=15)
    description: str
