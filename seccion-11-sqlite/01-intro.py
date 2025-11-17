# ref. v106

import sqlite3

# variable con -> objeto de conexion a db sqlite
# el metodo connect intentara conectarse con el archivo "seccion-11-sqlite/app.db"
# si el archivo "seccion-11-sqlite/app.db" no existe, py se va a encaragr de crearlo automaticamente
con = sqlite3.connect("seccion-11-sqlite/app.db")
con.close()
