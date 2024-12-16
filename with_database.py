import psycopg2
import config


def get_connection(func):
    def wrapper():
        with psycopg2.connect(
            host=config.db_host,
            user=config.db_user,
            password=config.db_password,
            database=config.db_name,
            port=config.db_port
        ) as connection:
            with connection.cursor() as cursor:
                # Подключается к БД и выполняет функцию передавая подключение
                result = func(cursor=cursor)
        return result
    return wrapper


@get_connection
def get_version(cursor):
    cursor.execute(
        "Select * from Notes;"
    )
    return cursor.fetchone()


def create_db(cursor):
    pass


def create_note(note_text):
    pass


# cursor.execute(
#     "Select version();"
# )

# print(cursor.fetchone())

# cursor.execute(
#     """INSERT INTO cases VALUES (1, 'Первая заметка');"""
# )

# connection.commit()

# cursor.execute(
#     """SELECT * FROM cases;"""
# )

# print(cursor.fetchone())

# except Exception as ex:
#     print(ex)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
