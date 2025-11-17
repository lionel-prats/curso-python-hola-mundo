# ref. v109

import sqlite3

# Cómo hackear una pagina web? | SQL INJECTION (HolaMundo YT) vvv
# https://www.youtube.com/watch?v=reI-Yh5PjTI
with sqlite3.connect("seccion-11-sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values (?, ?);",
        (266, "Alberto Casas")
    )
