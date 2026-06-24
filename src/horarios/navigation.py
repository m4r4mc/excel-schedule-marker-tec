"""Opciones de navegacion y funciones de entrada"""

ATRAS = "<<"
REINICIO = ">>"


class Reiniciar(Exception):
    """Se lanza para reiniciar todo el programa desde cero."""
    pass


class Retroceder(Exception):
    """Se lanza para volver al paso anterior."""
    pass


def ayuda_navegacion():
    print(f"  [{ATRAS} = atrás]   [{REINICIO} = reiniciar todo]")


def pedir_numero(prompt, opciones=None, permitir_cero=True):
    """Pide un entero. Acepta << (retroceder) y >> (reiniciar)."""
    while True:
        val = input(f"  › {prompt}: ").strip()
        if val == REINICIO:
            raise Reiniciar()
        if val == ATRAS:
            raise Retroceder()
        if permitir_cero and val == "0":
            return 0
        try:
            v = int(val)
        except ValueError:
            print("  ✗ Ingresá un número entero válido.")
            continue
        if opciones and v not in opciones:
            print("  ✗ Opción no válida.")
            continue
        return v


def pedir_texto(prompt, permitir_cero=False):
    """Pide texto. Acepta << (retroceder) y >> (reiniciar)."""
    while True:
        val = input(f"\n  › {prompt}: ").strip()
        if val == REINICIO:
            raise Reiniciar()
        if val == ATRAS:
            raise Retroceder()
        if permitir_cero and val == "0":
            return "0"
        if not val:
            print("  ✗ No puede estar vacío.")
            continue
        return val
