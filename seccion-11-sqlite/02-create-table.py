# ref. v107

import sqlite3

# variable con -> objeto de conexion a db sqlite
con = sqlite3.connect("seccion-11-sqlite/app.db")

# variable cursor -> objecto que va a funcionar como un intermediario entre la libreria sqlite3 y nosotros,
# que mediante él, podremos enviarle consulas sql a la db SQLite "seccion-11-sqlite/app.db"
cursor = con.cursor()

# usamos el metodo execute() del objecto cursor para realizar consultas SQL
cursor.execute(
    """
    create table if not exists usuarios 
    (id integer primary key, nombre varchar(50));
    """
)

# usamos el metodo commit() del objecto con para comprometer la consulta SQL contra la base de datos
# desde el objeto con, con el metodo commit(), estamos comprometiendo los cambios
con.commit()

con.close()
