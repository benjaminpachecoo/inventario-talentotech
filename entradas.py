from interfaz import Fore, mensaje_error


# Las funciones "pedir_" repiten la pregunta hasta recibir un dato válido.
# Si hay valor_actual (al actualizar), Enter lo conserva.
def pedir_texto(mensaje, obligatorio=True, valor_actual=None):
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        if valor_actual is not None:
            return valor_actual
        if not obligatorio:
            return ""
        mensaje_error("Este campo es obligatorio.")


def pedir_entero(mensaje, valor_actual=None, minimo=0):
    while True:
        texto = input(mensaje).strip()
        if not texto and valor_actual is not None:
            return valor_actual
        try:
            numero = int(texto)
            if numero < minimo:
                mensaje_error(f"El número debe ser mayor o igual a {minimo}.")
                continue
            return numero
        except ValueError:
            mensaje_error("Ingresá un número entero válido.")


def pedir_real(mensaje, valor_actual=None):
    while True:
        texto = input(mensaje).strip().replace(",", ".")
        if not texto and valor_actual is not None:
            return valor_actual
        try:
            numero = float(texto)
            if numero < 0:
                mensaje_error("El precio no puede ser negativo.")
                continue
            return numero
        except ValueError:
            mensaje_error("Ingresá un número válido (ej: 1500.50).")


def confirmar(mensaje):
    respuesta = input(Fore.YELLOW + f"{mensaje} (s/n): ").strip().lower()
    return respuesta == "s"
