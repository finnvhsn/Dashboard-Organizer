import sqlite3

def initialize_db():
    conn = sqlite3.connect('myusers.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY, username TEXT UNIQUE, email TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

def add_user(username, email, password):
    conn = sqlite3.connect('myusers.db')
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    finally:
        conn.close()




    
    