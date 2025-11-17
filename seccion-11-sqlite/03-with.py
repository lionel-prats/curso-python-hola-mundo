# ref. v108

import sqlite3

with sqlite3.connect("seccion-11-sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        create table if not exists usuarios 
        (id integer primary key, nombre varchar(50));
        """
    )
    # el metodo magico __exit__ del objeto con, se encarga en automatico de ejecutar los 2 metodos de abajo (es parte del comportamiento de la instruccion with de py)
    # con.commit()
    # con.close()
