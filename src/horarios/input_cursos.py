"""Pedir datos al usuario"""

from .constants import DIAS_SEM, HORARIOS_DB
from .navigation import pedir_num, pedir_text, ayuda_nav, Retroceder
from .ui import sub


def pedir_curso():
    """
    Pide los datos del curso: nombre, cantidad de dias, duración, grupos
    Cambia de curso si el usuario digita 0
    Puede reiniciar el programa o retroceder
    """
    while True:
        try:
            nombre = pedir_text(
                "Nombre del curso (0 para terminar, << atrás, >> reiniciar todo)",
                t_cero=True,
            )
            if nombre == "0":
                return None

            sub("Configuración del curso")
            ayuda_nav()
            tipo = pedir_num("Tipo: 1. 1 día/semana o 2. 2 días/semana", [1, 2], t_cero=False)
            dur_op = pedir_num("Duración: 1. 1h 50m, 2. 2h 50m, 3. 3h 50m", [1, 2, 3], t_cero=False)
            dur = [110, 170, 230][dur_op - 1]

            grupos = []

            while True:
                try:
                    ayuda_nav()
                    num = pedir_num(f"Número de grupo para {nombre} (0 para terminar)")
                    if num == 0:
                        if not grupos:
                            print("  Ingrese al menos un grupo antes de terminar.")
                            continue
                        break

                    sub(f"Grupo {num}")

                    ayuda_nav()
                    if tipo == 2:
                        dias = (
                            ["Martes", "Jueves"]
                            if pedir_num("1. K/J | 2. M/V", [1, 2], t_cero=False) == 1
                            else ["Miércoles", "Viernes"]
                        )
                    else:
                        for i, d in enumerate(DIAS_SEM, 1):
                            print(f"    {i}. {d}")
                        dias = [DIAS_SEM[pedir_num("Seleccione un día", list(range(1, 7)), t_cero=False) - 1]]

                    opciones = [h for h in HORARIOS_DB if h["dur"] == dur]

                    for i, h in enumerate(opciones, 1):
                        print(f"    {i}. {h['ini']} – {h['fin']}")

                    ayuda_nav()
                    h = opciones[pedir_num("Seleccione horario", list(range(1, len(opciones) + 1)), t_cero=False) - 1]
                    interes = pedir_num("Interés (1-10)", list(range(1, 11)), t_cero=False)

                    grupos.append({"num": num, "dias": dias, "horario": h, "interes": interes})
                    print(f"  Grupo {num} agregado.")

                except Retroceder:
                    if grupos:
                        eliminado = grupos.pop()
                        print(f"  Grupo {eliminado['num']} eliminado. Vuelva a ingresarlo.")
                    else:
                        print("  (Volviendo a la configuración del curso)")
                        raise

            return {"nombre": nombre, "grupos": grupos}

        except Retroceder:
            print("  (Volviendo a ingresar este curso desde el nombre)")
            continue


def ingresar_cursos():
    cursos = []
    while True:
        try:
            resultado = pedir_curso()
            if resultado is None:
                if not cursos:
                    print("  Ingrese al menos un curso antes de terminar.")
                    continue
                break
            cursos.append(resultado)
            print(f"   Curso '{resultado['nombre']}' registrado con {len(resultado['grupos'])} grupo(s).")
        except Retroceder:
            if cursos:
                eliminado = cursos.pop()
                print(f" Curso '{eliminado['nombre']}' eliminado. Volvés a ingresarlo.")
            else:
                print(" No hay cursos para retroceder.")
            continue

    return cursos
