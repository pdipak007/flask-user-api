import sqlite3

conn = sqlite3.connect("db/users.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Database initialized with users table.")
