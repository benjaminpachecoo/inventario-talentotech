try:
    from colorama import Fore, Style, init

    init(autoreset=True)
except ImportError:
    class _SinColor:
        def __getattr__(self, _nombre):
            return ""

    Fore = Style = _SinColor()

# Opciones del menú con color propio (el resto usa el estilo por defecto)
COLORES_OPCION = {
    "0": Fore.RED,
}

# Por debajo de este valor la cantidad se muestra en rojo; desde acá, en verde
STOCK_MINIMO = 10


def mensaje_ok(texto):
    print(Fore.GREEN + "✔ " + texto)


def mensaje_error(texto):
    print(Fore.RED + "✘ " + texto)


def mensaje_info(texto):
    print(Fore.YELLOW + texto)


def titulo(texto):
    print()
    print(Fore.CYAN + Style.BRIGHT + f"=== {texto} ===")


def mostrar_menu(opciones):
    titulo("GESTIÓN DE INVENTARIO")
    for tecla, descripcion in opciones:
        color = COLORES_OPCION.get(tecla)
        if color:
            print(color + f"{tecla}. {descripcion}")
        else:
            print(Fore.CYAN + f"{tecla}." + Style.RESET_ALL + f" {descripcion}")


def mostrar_productos(productos):
    if not productos:
        mensaje_info("No se encontraron productos.")
        return

    encabezado = f"{'ID':<5}{'Nombre':<20}{'Descripción':<28}{'Cant.':>7}{'Precio':>12}  {'Categoría':<15}"
    print(Style.BRIGHT + encabezado)
    print("-" * len(encabezado))
    for id_, nombre, descripcion, cantidad, precio, categoria in productos:
        color_cantidad = Fore.RED if cantidad < STOCK_MINIMO else Fore.GREEN
        print(
            f"{id_:<5}{nombre[:19]:<20}{(descripcion or '')[:27]:<28}"
            f"{color_cantidad}{cantidad:>7}{Style.RESET_ALL}"
            f"{precio:>12.2f}  {(categoria or '')[:15]:<15}"
        )
    print(f"\nTotal: {len(productos)} producto(s).")
