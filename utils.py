import json
import sqlite3 as sql


def load_data():
        connection = sql.connect('static/data/notes.db')
        cursor = connection.cursor()
        read = '''SELECT * FROM notes'''
        cursor.execute(read)
        return cursor.fetchall()
        
    

def load_templates(file_path):
    with open(f"static/templates/{file_path}", "r") as f:
        response = f.read()
        return response

def add_to_db(title, detail):
    connection = sql.connect('static/data/notes.db')
    cursor = connection.cursor()
    add = f'''INSERT INTO notes (TITULO, DETALHES) VALUES ("{title}", "{detail}");'''
    cursor.execute(add)
    connection.commit()
    connection.close()


def create_db():
    con = sql.connect('notes.db')

    cur = con.cursor()

    cur.execute("DROP TABLE IF EXISTS notes")

    sqlaite = ''' CREATE TABLE "notes" (
                "TITULO" TEXT,
                "DETALHES" TEXT,
                "ID" INTEGER PRIMARY KEY AUTOINCREMENT 
                )'''

    cur.execute(sqlaite)

    con.commit()
    con.close()

def delete_from_db(id):
    connection = sql.connect('static/data/notes.db')
    cursor = connection.cursor()
    delete = f'''DELETE FROM notes WHERE ID = '{id}';'''
    cursor.execute(delete)
    connection.commit()
    connection.close()