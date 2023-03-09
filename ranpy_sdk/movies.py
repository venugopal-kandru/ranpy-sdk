import sys
import sqlite3

CREATE_TABLE = '''
CREATE TABLE movies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
'''

DEFAULT_DB = 'ranpy_sdk.db'

class Movie:
    def __init__(self, db=DEFAULT_DB):
        pass

    def list_movies(self):
        pass

    def add_movie(self):
        pass

    def del_movie(self):
        pass

    def update_movie(self):
        pass

    def get_movie(self):
        pass

