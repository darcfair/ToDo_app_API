import psycopg2
import config
import db_request


def get_connection(func):
    """Декоратор для подключения к базе данных"""

    def wrapper():
        try:
            with psycopg2.connect(
                host=config.db_host,
                user=config.db_user,
                password=config.db_password,
                database=config.db_name,
                port=config.db_port
            ) as connection:
                with connection.cursor() as cursor:
                    # Передаёт подключение к db в функцию
                    result = {
                        "Connection": True,
                        "Reply": func(cursor=cursor)
                        }
        except Exception as ex:
            result = {
                "Connection": False,
                "Reply": {"Error": str(ex)}}
        return result
    return wrapper


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
def get_note_db_with_id(cursor, id):
    """Получение заметки по id"""
    cursor.execute(db_request.select_note.format(id=id))
    return cursor.fetchall()


@get_connection
def create_new_note(cursor, name, description):
    """Создание новой заметки"""
    cursor.execute(db_request.create_note.format(
        note_name=name,
        description=description
        ))
    return cursor.fetchall()
