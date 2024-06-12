import sqlite3
from sqlite3 import Error


# create invoice table
def create_invoice_table(db_file):
    # Create a cursor object
    conn = sqlite3.connect(db_file)

    # Create a a cursor object
    cursor = conn.cursor()
      
    # Create a invoice table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS invoices (
        id INTEGER PRIMARY KEY,
        room_name TEXT,
        room_type TEXT,
        room_rate INTEGER,
        room_user_id TEXT,
        month TEXT,
        year INTEGER,
        FOREIGN KEY (room_name) REFERENCES rooms(name),
        FOREIGN KEY (room_type) REFERENCES rooms(room_type),
        FOREIGN KEY (room_rate) REFERENCES rates(rate),
        FOREIGN KEY (room_user_id) REFERENCES rooms(user_id)
    )
    ''')
    conn.commit()
    conn.close()


def create_invoice_by_room(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.name, rooms.room_type, rates.rate, users.name FROM rooms INNER JOIN users ON users.id = rooms.user_id INNER JOIN rates ON rooms.room_type = rates.name WHERE rooms.name = ?', (name,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def query_invoice_all(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.name, rooms.room_type, rates.rate, users.name FROM rooms INNER JOIN users ON users.id = rooms.user_id INNER JOIN rates ON rooms.room_type = rates.name ORDER BY rooms.name')
    rows = cursor.fetchall()
    conn.close()
    return rows


def query_invoice_all_with_date(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT room_user_id, room_name, room_type, room_rate, month, year FROM invoices ORDER BY room_user_id')
    rows = cursor.fetchall()
    conn.close()
    return rows

def query_invoice_by_user(db_file, room_user_id):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT room_user_id, room_name, room_type, room_rate, month, year FROM invoices WHERE room_user_id = ?', (room_user_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows


def query_invoice_by_user_with_date(db_file, room_user_id, month, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT room_user_id, room_name, room_type, room_rate, month, year FROM invoices WHERE room_user_id = ? AND month = ? AND year = ?', (room_user_id, month, year))
    rows = cursor.fetchall()
    conn.close()
    return rows

def create_invoice_all_by_month(db_file, month, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.name, rooms.room_type, rates.rate, users.name FROM rooms INNER JOIN users ON users.id = rooms.user_id INNER JOIN rates ON rooms.room_type = rates.name ORDER BY rooms.name')
    rows = cursor.fetchall()
    for room_name, room_type, room_rate, room_user_id in rows:
        if not invoice_exists(db_file, room_name):
            print("{info - start insert invoices data}")
            cursor.execute('''
            INSERT INTO invoices (room_name, room_type, room_rate, room_user_id) VALUES (?, ?, ?, ?)
            ''', (room_name, room_type, room_rate, room_user_id))
            print("{info - done insert invoices data}")
    conn.commit()
    for room_name, room_type, room_rate, room_user_id in rows:
        if not invoice_exists(db_file, month):
            print("{info - start update invoices data}")
            cursor.execute('UPDATE invoices SET month = ?, year = ? WHERE month IS NULL AND year IS NULL', (month, year))
            print("{info - done update invoices data}")
    conn.commit()
    conn.close()
    return rows

def create_invoice_all_by_month_test(db_file, month, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT rooms.name, rooms.room_type, rates.rate, users.name FROM rooms INNER JOIN users ON users.id = rooms.user_id INNER JOIN rates ON rooms.room_type = rates.name ORDER BY rooms.name')
    rows = cursor.fetchall()
    for room_name, room_type, room_rate, room_user_id in rows:
        if not invoice_exists_by_month(db_file, month, year):
            print("{info - start insert invoices data}")
            cursor.execute('''
            INSERT INTO invoices (room_name, room_type, room_rate, room_user_id, month, year) VALUES (?, ?, ?, ?, ?, ?)
            ''', (room_name, room_type, room_rate, room_user_id, month, year))
            print("{info - done insert invoices data}")
    conn.commit()
    conn.close()
    return rows

def invoice_exists(db_file, name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM invoices WHERE room_name = ?', (name,))
    return cursor.fetchone() is not None

def invoice_exists_by_month(db_file, month_name, year):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM invoices WHERE month = ? AND year = ?', (month_name, year))
    return cursor.fetchone() is not None
