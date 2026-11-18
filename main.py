import productos
from base_datos import crear_tabla
from interfaz import mensaje_error, mensaje_info, mensaje_ok, mostrar_menu

# Cada opción del menú: tecla -> (texto, función que ejecuta)
OPCIONES = {
    "1": ("Registrar producto", productos.registrar_producto),
    "2": ("Ver productos", productos.ver_productos),
    "3": ("Actualizar producto", productos.actualizar_producto),
    "4": ("Eliminar producto", productos.eliminar_producto),
    "5": ("Buscar producto", productos.buscar_producto),
    "6": ("Reporte de bajo stock", productos.reporte_bajo_stock),
}


def main():
    crear_tabla()

    items_menu = [(tecla, texto) for tecla, (texto, _) in OPCIONES.items()]
    items_menu.append(("0", "Salir"))

    while True:
        mostrar_menu(items_menu)
        opcion = input("\nElegí una opción: ").strip()
        if opcion == "0":
            mensaje_ok("¡Hasta luego!")
            break
        if opcion in OPCIONES:
            _, accion = OPCIONES[opcion]
            accion()
        else:
            mensaje_error("Opción inválida. Probá de nuevo.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        # Salida prolija con Ctrl+C
        print()
        mensaje_info("Programa interrumpido. ¡Hasta luego!")
