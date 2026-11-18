import base_datos as bd
from entradas import confirmar, pedir_entero, pedir_real, pedir_texto
from interfaz import mensaje_error, mensaje_info, mensaje_ok, mostrar_productos, titulo


def registrar_producto():
    titulo("Registrar producto")
    nombre = pedir_texto("Nombre: ")
    descripcion = pedir_texto("Descripción (opcional): ", obligatorio=False)
    cantidad = pedir_entero("Cantidad: ")
    precio = pedir_real("Precio: ")
    categoria = pedir_texto("Categoría (opcional): ", obligatorio=False)

    nuevo_id = bd.insertar_producto(nombre, descripcion, cantidad, precio, categoria)
    mensaje_ok(f"Producto registrado con ID {nuevo_id}.")


def ver_productos():
    titulo("Listado de productos")
    mostrar_productos(bd.listar_productos())


def actualizar_producto():
    titulo("Actualizar producto")
    id_producto = pedir_entero("ID del producto a actualizar: ", minimo=1)
    producto = bd.obtener_producto(id_producto)
    if producto is None:
        mensaje_error(f"No existe un producto con ID {id_producto}.")
        return

    mostrar_productos([producto])
    mensaje_info("\nIngresá los nuevos datos (Enter para conservar el valor actual):")
    _, nombre, descripcion, cantidad, precio, categoria = producto
    descripcion = descripcion or ""
    categoria = categoria or ""

    nombre = pedir_texto(f"Nombre [{nombre}]: ", valor_actual=nombre)
    descripcion = pedir_texto(f"Descripción [{descripcion}]: ", valor_actual=descripcion)
    cantidad = pedir_entero(f"Cantidad [{cantidad}]: ", valor_actual=cantidad)
    precio = pedir_real(f"Precio [{precio}]: ", valor_actual=precio)
    categoria = pedir_texto(f"Categoría [{categoria}]: ", valor_actual=categoria)

    bd.actualizar_producto(id_producto, nombre, descripcion, cantidad, precio, categoria)
    mensaje_ok("Producto actualizado correctamente.")


def eliminar_producto():
    titulo("Eliminar producto")
    id_producto = pedir_entero("ID del producto a eliminar: ", minimo=1)
    producto = bd.obtener_producto(id_producto)
    if producto is None:
        mensaje_error(f"No existe un producto con ID {id_producto}.")
        return

    mostrar_productos([producto])
    if not confirmar("¿Seguro que querés eliminarlo?"):
        mensaje_info("Eliminación cancelada.")
        return

    bd.eliminar_producto(id_producto)
    mensaje_ok("Producto eliminado.")


def buscar_producto():
    titulo("Buscar producto")
    print("1. Por ID")
    print("2. Por nombre")
    print("3. Por categoría")
    opcion = input("Elegí una opción: ").strip()

    if opcion == "1":
        id_producto = pedir_entero("ID: ", minimo=1)
        producto = bd.obtener_producto(id_producto)
        resultados = [producto] if producto else []
    elif opcion in ("2", "3"):
        campo = "nombre" if opcion == "2" else "categoria"
        termino = pedir_texto(f"Texto a buscar en {campo}: ")
        resultados = bd.buscar_por_campo(campo, termino)
    else:
        mensaje_error("Opción inválida.")
        return

    mostrar_productos(resultados)


def reporte_bajo_stock():
    titulo("Reporte de bajo stock")
    limite = pedir_entero("Mostrar productos con cantidad menor o igual a: ")
    mostrar_productos(bd.productos_bajo_stock(limite))
