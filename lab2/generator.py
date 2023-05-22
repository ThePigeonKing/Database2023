import random
import sqlite3
import sys

from math import log

import models

def create_connect(db_path: str) -> sqlite3.Connection:
    connection = sqlite3.connect(db_path)
    return connection

def get_cursor(conn: sqlite3.Connection) -> sqlite3.Cursor:
    return conn.cursor()

def init_db(conn: sqlite3.Connection) -> None:
    curs = get_cursor(conn)
    with open("../lab1/db_init_sqlite.sql") as f:
        curs.execute(f.read)
    
    conn.commit()

