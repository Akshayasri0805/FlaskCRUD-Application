import sqlite3

def init_sqlite_db():
    conn = sqlite3.connect('database.db')
    print("Opened database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
    print("Table created successfully")
    conn.close()

if __name__ == '__main__':
    init_sqlite_db()
