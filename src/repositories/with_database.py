
from src.repositories import db_request
from src.repositories.connection import get_connection
from src.schemas import Note


@get_connection
def get_version_db(cursor):
    """API для проверки подключения"""
    cursor.execute(db_request.select_version)
    return cursor.fetchone()


@get_connection
def create_table_note(cursor):
    """Создание таблицы при создании приложения"""
    cursor.execute(db_request.create_table_note)
    return cursor.fetchall()


@get_connection
def get_all_notes_db(cursor):
    """Получение всех заметок"""
    cursor.execute(db_request.select_all_notes)
    return cursor.fetchall()


@get_connection
def get_note_db_with_id(cursor, id: int):
    """Получение заметки по id"""
    cursor.execute(db_request.select_note.format(id=id))
    return cursor.fetchall()


@get_connection
def get_note_db_with_name(cursor, name: str):
    """Получение заметки по имени"""
    cursor.execute(db_request.select_note_by_name.format(name=name))
    return cursor.fetchall()


@get_connection
def create_new_note_db(cursor, note: Note):
    """Создание новой заметки"""
    cursor.execute(db_request.create_note.format(
        name=note.name,
        description=note.description
        ))
    return "Sucsess"


@get_connection
def delete_note_db_with_id(cursor, id: int):
    """Удаление заметки по id"""
    cursor.execute(db_request.delete_note_by_id.format(
        id=id
        ))
    return "Sucsess"
