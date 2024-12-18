select_version = '''SELECT version();'''

select_all_notes = '''SELECT * FROM notes;'''

select_note = (
    'SELECT * FROM notes\n'
    'WHERE notes.id={id};'
)

create_table_note = (
    '''CREATE TABLE IF NOT EXISTS notes (
note_id SERIAL PRIMARY KEY,
note_name VARCHAR(20),
note_description TEXT NULL);

INSERT INTO notes
SELECT 1, 'Первая заметка', 'Описание первой заметки' WHERE NOT EXISTS (
SELECT * FROM notes);'''
)

create_note = (
    'INSERT INTO notes VALUES (\n'
    "DEFAULT, '{name}', '{description}');"
)
