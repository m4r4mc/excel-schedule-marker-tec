#!/usr/bin/env python3
"""
Generador de Horarios — punto de entrada del programa.
Ejecutar con: python main.py
"""

from src.horarios.ui import limpiar, titulo
from src.horarios.nav import Reiniciar, ATRAS, REINICIO
from src.horarios.input_cursos import ingresar_cursos
from src.horarios.excel import generar_excel


def ejecutar():
    limpiar()
    titulo("GENERADOR DE HORARIOS")
    print("  Instrucciones: ingresá tus cursos y grupos. En cualquier momento podés")
    print(f"  escribir {ATRAS} para corregir el paso anterior, o {REINICIO} para")
    print("  reiniciar todo el programa desde cero.\n")

    cursos = ingresar_cursos()
    if cursos:
        generar_excel(cursos)


def main():
    while True:
        try:
            ejecutar()
            break
        except Reiniciar:
            limpiar()
            print("\n Reiniciando todo el programa desde cero...\n")
            continue


if __name__ == "__main__":
    main()
