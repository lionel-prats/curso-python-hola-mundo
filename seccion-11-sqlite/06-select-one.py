# ref. v111

import sqlite3
import os
os.system('cls' if os.name == 'nt' else 'clear')

with sqlite3.connect("seccion-11-sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("select * from usuarios")

    print(type(cursor.fetchone()))
    print(cursor.fetchone())
