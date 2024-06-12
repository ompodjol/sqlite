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
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
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
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        name TEXT NOT NULL,
        room_type TEXT,
        description TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (room_type) REFERENCES rates(name)
    )
    ''')
    conn.commit()
    conn.close()


# Create rate table
def create_rate_table(db_file):
    # Create a cursor object
    conn = sqlite3.connect(db_file)

    # Create a a cursor object
    cursor = conn.cursor()
      
    # Create a room rate table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rates (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        rate REAL NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

    
def insert_user(db_file, user_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for name, age in user_data:
        if not user_exists(db_file, name):
            print("{info - start insert user data}")
            cursor.execute('''
            INSERT INTO users (name, age) VALUES (?, ?)
            ''', (name, age))
            print("{info - done insert user data}")
    conn.commit()
    conn.close()


def insert_room(db_file, room_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for name, description in room_data:
        if not room_exists(db_file, name):
            print("{info - start insert room data}")
            cursor.execute('''
            INSERT INTO rooms (name, description) VALUES (?, ?)
            ''', (name, description))
            print("{info - done insert room data}")
    conn.commit()
    conn.close()


def insert_rate(db_file, room_rate):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for name, rate in room_rate:
        if not rate_exists(db_file, name):
            print("{info - start insert room rate data}")
            cursor.execute('''
            INSERT INTO rates (name, rate) VALUES (?, ?)
            ''', (name, rate))
            print("{info - done insert room rate data}")
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


def user_exists(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE name = ?', (name,))
    return cursor.fetchone() is not None


def room_exists(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM rooms WHERE name = ?', (name,))
    return cursor.fetchone() is not None


def rate_exists(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM rates WHERE name = ?', (name,))
    return cursor.fetchone() is not None

               
def delete_user(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.commit()
    conn.close()


def update_user_age(db_file, name, new_age):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
    conn.commit()
    conn.close()


def update_room_user(db_file, name, user_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE rooms SET user_id = ? WHERE name = ?', (user_id, name))
    conn.commit()
    conn.close()


def update_room_type(db_file, name, room_type):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('UPDATE rooms SET room_type = ? WHERE name = ?', (room_type, name))
    conn.commit()
    conn.close()

    
def read_room_user(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.name, rooms.description, users.name FROM rooms INNER JOIN users ON users.id = rooms.user_id WHERE rooms.name = ?', (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_room_by_room_name(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT name, description, user_id FROM rooms WHERE name = ?', (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def read_room_rate_by_name(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.name, rooms.room_type, rates.name, rates.rate FROM rooms INNER JOIN rates ON rates.name = rooms.room_type WHERE rooms.name = ?', (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def update_room_rate_by_variable(db_file, room_rate):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for name, room_type in room_rate:
        if not rate_exists(db_file, name):
            print("{info - start update room type data}")
            cursor.execute('UPDATE rooms SET room_type = ? WHERE name = ?', (room_type, name))
            print("{info - done update room type data}")
    conn.commit()
    conn.close()
