"""Funciones para choques de cursos"""


def choque(combo):
    ocupado = {}
    for g in combo:
        for d in g["dias"]:
            if d not in ocupado:
                ocupado[d] = []
            for ini, fin in ocupado[d]:
                a1, a2 = g["horario"]["ini_m"], g["horario"]["fin_m"]
                if not (a2 <= ini or a1 >= fin):
                    return True
            ocupado[d].append((g["horario"]["ini_m"], g["horario"]["fin_m"]))
    return False
