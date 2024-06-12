import sqlite3
from sqlite3 import Error


# create month table
def create_calendar_table(db_file):
    # Create a cursor object
    conn = sqlite3.connect(db_file)

    # Create a a cursor object
    cursor = conn.cursor()
      
    # Create month table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS calendar (
        id INTEGER PRIMARY KEY,
        month TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


# Create month calendar object
def insert_month(db_file, calendar_data):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    for id, month in calendar_data:
        if not month_exists(db_file, month):
            print("{info - start insert calendar data}")
            cursor.execute('''
            INSERT INTO calendar (id, month) VALUES (?, ?)
            ''', (id, month))
            print("{info - done insert calendar data}")
    conn.commit()
    conn.close()


def month_exists(db_file, month):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM calendar WHERE month = ?', (month,))
    return cursor.fetchone() is not None
