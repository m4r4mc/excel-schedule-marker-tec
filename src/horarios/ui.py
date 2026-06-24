"""Funciones de interfaz"""

import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")


def titulo(t):
    print(f"\n╔{'═'*62}╗\n║{t.center(62)}║\n╚{'═'*62}╝")


def sub(t):
    print(f"\n ▸ {t}\n  {'─'*(len(t)+2)}")
