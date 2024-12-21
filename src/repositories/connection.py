import psycopg2
from src import config


def get_connection(func):
    """Декоратор для подключения к базе данных"""

    def wrapper(*args, **kwargs):
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
                        "Reply": (func(cursor=cursor, *args, **kwargs))
                        }
        except Exception as ex:
            print(ex.args)
            result = {
                "Connection": False,
                "Reply": {"Error": str(ex)}}
        return result
    return wrapper
