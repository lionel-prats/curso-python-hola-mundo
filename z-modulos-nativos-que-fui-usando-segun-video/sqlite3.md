## `MODULO sqlite3` (video 106)
### Para qué sirve
El módulo sqlite3 proporciona una interfaz nativa para trabajar con SQLite, una base de datos relacional liviana, embebida y basada en archivos.   
SQLite no requiere un servidor ni servicios externos: toda la base de datos reside en un único archivo .db y puede ser creada, modificada y consultada directamente desde Python.

Con este módulo es posible:
- Crear bases de datos y conectarse a ellas mediante sqlite3.connect().
- Ejecutar consultas SQL (SELECT, INSERT, UPDATE, DELETE, CREATE TABLE, etc.) utilizando cursores (cursor).
- Gestionar transacciones con commit() y rollback() para mantener la integridad de los datos.
- Leer resultados de consultas en forma de tuplas, listas o diccionarios.
- Crear aplicaciones completas que persisten datos sin necesidad de instalar MySQL, PostgreSQL o un servidor externo.
- Prototipar rápidamente sistemas que más tarde podrían migrarse a una base de datos más robusta.
- Integrar almacenamiento ligero en herramientas locales, scripts automatizados, aplicaciones de escritorio, proyectos educativos y pruebas.

SQLite es extremadamente confiable, rápido y portátil, por lo que este módulo es ideal cuando se necesita persistencia real sin la complejidad de un motor de base de datos tradicional.

### Ejemplo
```python
import sqlite3

# variable con -> objeto de conexion a db sqlite
# el metodo connect intentara conectarse con el archivo "seccion-11-sqlite/app.db"
# si el archivo "seccion-11-sqlite/app.db" no existe, py se va a encaragr de crearlo automaticamente
con = sqlite3.connect("seccion-11-sqlite/app.db")
con.close()
```