import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
        
        # Enable foreign key support
        conn.execute('PRAGMA foreign_keys = ON')
    
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


# create user table
def create_user_table(db_file):
    # Create a cursor object
    conn = sqlite3.connect(db_file)

    # Create a a cursor object
    cursor = conn.cursor()
      
    # Create a user table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL,
        user_age INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


# Create room table
def create_room_table(db_file):
    # Create a cursor object
    conn = sqlite3.connect(db_file)

    # Create a a cursor object
    cursor = conn.cursor()
      
    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rooms (
        room_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        room_name TEXT NOT NULL,
        room_description TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')
    conn.commit()
    conn.close()

    
def insert_user(db_file, user_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for user_name, user_age in user_data:
        if not user_exists(db_file, user_name):
            print("{info - start insert user data}")
            cursor.execute('''
            INSERT INTO users (user_name, user_age) VALUES (?, ?)
            ''', (user_name, user_age))
            print("{info - done insert user data}")
    conn.commit()
    conn.close()


def insert_room(db_file, room_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for room_name, room_description in room_data:
        if not user_exists(db_file, room_name):
            print("{info - start insert room data}")
            cursor.execute('''
            INSERT INTO rooms (room_name, room_description) VALUES (?, ?)
            ''', (room_name, room_description))
            print("{info - done insert room data}")
    conn.commit()
    conn.close()

    
def read_user(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_room(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM rooms')
    rows = cursor.fetchall()
    conn.close()
    return rows


def user_exists(db_file, user_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE user_name = ?', (user_name,))
    return cursor.fetchone() is not None

               
def delete_user(db_file, user_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE user_name = ?', (user_name,))
    conn.commit()
    conn.close()


def update_user_age(db_file, user_name, new_user_age):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET user_age = ? WHERE user_name = ?', (new_user_age, user_name))
    conn.commit()
    conn.close()


def update_room_user(db_file, room_name, user_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE rooms SET user_id = ? WHERE room_name = ?', (user_id, room_name))
    conn.commit()
    conn.close()

    
def read_room_user(db_file, room_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.room_name, rooms.room_description, users.user_name FROM rooms INNER JOIN users ON users.user_id = rooms.user_id WHERE room_name = ?', (room_name,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_room_by_room_name(db_file, room_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT room_name, room_description, user_id FROM rooms WHERE room_name = ?', (room_name,))
    rows = cursor.fetchall()
    conn.close()
    return rows
