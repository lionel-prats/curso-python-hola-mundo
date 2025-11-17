# ref. v110

import sqlite3

with sqlite3.connect("seccion-11-sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (292, "Lionel Prats"),
        (317, "Valentina Jaime"),
        (1042, "Andrés Bruno")
    ]
    cursor.executemany(
        "insert into usuarios values (?, ?);",
        usuarios
    )
