import os
import sqlite3

# La base se guarda en la misma carpeta que este archivo
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inventario.db")

# Únicos campos permitidos para buscar por texto
CAMPOS_BUSQUEDA = ("nombre", "categoria")


def conectar():
    return sqlite3.connect(DB_PATH)


def crear_tabla():
    with conectar() as conexion:
        conexion.execute(
            """
            CREATE TABLE IF NOT EXISTS productos (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre      TEXT    NOT NULL,
                descripcion TEXT,
                cantidad    INTEGER NOT NULL,
                precio      REAL    NOT NULL,
                categoria   TEXT
            )
            """
        )


def insertar_producto(nombre, descripcion, cantidad, precio, categoria):
    # Los "?" pasan los valores aparte y evitan la inyección SQL
    with conectar() as conexion:
        cursor = conexion.execute(
            "INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria) "
            "VALUES (?, ?, ?, ?, ?)",
            (nombre, descripcion, cantidad, precio, categoria),
        )
        return cursor.lastrowid


def listar_productos():
    with conectar() as conexion:
        return conexion.execute("SELECT * FROM productos ORDER BY id").fetchall()


def obtener_producto(id_producto):
    with conectar() as conexion:
        cursor = conexion.execute("SELECT * FROM productos WHERE id = ?", (id_producto,))
        return cursor.fetchone()


def actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria):
    with conectar() as conexion:
        conexion.execute(
            "UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, "
            "precio = ?, categoria = ? WHERE id = ?",
            (nombre, descripcion, cantidad, precio, categoria, id_producto),
        )


def eliminar_producto(id_producto):
    with conectar() as conexion:
        conexion.execute("DELETE FROM productos WHERE id = ?", (id_producto,))


def buscar_por_campo(campo, termino):
    if campo not in CAMPOS_BUSQUEDA:
        raise ValueError(f"Campo de búsqueda no permitido: {campo}")
    # LIKE con % encuentra coincidencias parciales (ej: "yer" -> "Yerba")
    with conectar() as conexion:
        return conexion.execute(
            f"SELECT * FROM productos WHERE {campo} LIKE ? ORDER BY id",
            (f"%{termino}%",),
        ).fetchall()


def productos_bajo_stock(limite):
    with conectar() as conexion:
        return conexion.execute(
            "SELECT * FROM productos WHERE cantidad <= ? ORDER BY cantidad, id",
            (limite,),
        ).fetchall()
