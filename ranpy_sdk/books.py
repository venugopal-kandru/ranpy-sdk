import sys
import re
import json
import sqlite3

CREATE_TABLE = '''
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
'''

DEFAULT_DB = 'ranpy_sdk.db'

class Book:
    '''
    An object to interact with the book database.
    '''
    def __init__(self, db=DEFAULT_DB):
        self.db = db
        self.create_table()
        self.conn = None

    def get_conn(self):
        if self.conn is not None:
            return self.conn

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        return conn, cursor

    def create_table(self):
        # Establish a connection to the database
        conn = sqlite3.connect(self.db)

        # Create a cursor object
        cursor = conn.cursor()

        # Execute the CREATE TABLE statement
        cursor.execute(CREATE_TABLE)

        # Commit the transaction
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

    def list_books(self):
        '''
        List out all the books available in the datbase to read.
        '''
        conn, cur = self.get_conn()
        cur.execute('select * from books')
        books = [ book for book in cur.fetchall() ]

        return books

    def add_book(self, name):
        '''
        Add a new book to the database.

        :param: name
        '''
        conn, cur = self.get_conn()
        cur.execute('INSERT INTO books (id, name) VALUES (1, "%s")' % name)
        conn.commit()

    def del_book(self):

        conn, cur = self.get_conn()

    def get_book(self):
        conn, cur = self.get_conn()

    def update_book(self):
        conn, cur = self.get_conn()

    def total_books(self):
        conn, cur = self.get_conn()
