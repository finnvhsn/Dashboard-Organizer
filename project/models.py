import sqlite3
from werkzeug.security import check_password_hash

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

def check_user(username, password):
    conn = sqlite3.connect('myusers.db')
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        user_data = cursor.fetchone()
        
        if user_data and check_password_hash(user_data[3], password):
            # Erstelle ein User-Objekt mit den Daten aus der Datenbank
            user = user_data[0]
            return user
        else:
            return None
    finally:
        conn.close()

    
    