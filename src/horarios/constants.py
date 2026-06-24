"""Constantes usadas: días, horarios y colores"""

DIAS_SEM = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"]

#horarios fijos disponibles, agrupados por duración (en minutos).
HORARIOS_DB = [
    {"ini": "7:30", "fin": "9:20", "dur": 110, "ini_m": 450, "fin_m": 560},
    {"ini": "9:30", "fin": "11:20", "dur": 110, "ini_m": 570, "fin_m": 680},
    {"ini": "1:00", "fin": "2:50", "dur": 110, "ini_m": 780, "fin_m": 890},
    {"ini": "3:00", "fin": "4:50", "dur": 110, "ini_m": 900, "fin_m": 1010},
    {"ini": "5:00", "fin": "6:50", "dur": 110, "ini_m": 1020, "fin_m": 1130},
    {"ini": "7:00", "fin": "8:50", "dur": 110, "ini_m": 1140, "fin_m": 1250},

    {"ini": "7:30", "fin": "10:20", "dur": 170, "ini_m": 450, "fin_m": 620},
    {"ini": "9:30", "fin": "12:20", "dur": 170, "ini_m": 570, "fin_m": 740},
    {"ini": "5:00", "fin": "7:50", "dur": 170, "ini_m": 1020, "fin_m": 1190},
    {"ini": "8:30", "fin": "11:20", "dur": 170, "ini_m": 510, "fin_m": 680},

    {"ini": "7:30", "fin": "11:20", "dur": 230, "ini_m": 450, "fin_m": 680},
    {"ini": "1:00", "fin": "4:50", "dur": 230, "ini_m": 780, "fin_m": 1010},
    {"ini": "5:00", "fin": "8:50", "dur": 230, "ini_m": 1020, "fin_m": 1250},
]

COLORES = ["FF6B6B", "4D96FF", "6BCB77", "FFD93D", "845EC2", "FF9671", "00C9A7"]
