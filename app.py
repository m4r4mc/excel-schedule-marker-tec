"""
Generador de Horarios: version web
"""

import io
import streamlit as st
from itertools import product
from src.horarios.constants import DIAS_SEM, HORARIOS_DB
from src.horarios.combinaciones import choque
from src.horarios.excel import generar_excel

st.set_page_config(page_title="Generador de Horarios", layout="centered")

if "cursos" not in st.session_state:
    st.session_state.cursos = []

TLABELS = {110: "1h 50min", 170: "2h 50 min", 230: "3h 50min"}
D_2 = {"Martes y Jueves": ["Martes", "Jueves"], "Miercoles y Viernes": ["Miercoles", "Viernes"]}

st.title("Generador de horarios - TEC")
st.caption("Digite el curso y su informacion respectiva, la app genera un excel con todas las combinaciones de horarios disponibles")

#interfaz para agregar un nuevo curso
st.header("1. Agregar un curso")
with st.form("form_curso", clear_on_submit=True):
    nom_curso = st.text_input("Nombre del curso")
    col1, col2 = st.columns(2)
    with col1:
        tipo = st.radio("Días por semana", ["1 día", "2 días"], horizontal=True)
    with col2:
        dur_label = st.radio("Duración de cada sesión", list(TLABELS.values()), horizontal=True)
    dur = [k for k, v in TLABELS.items() if v == dur_label][0]

    anotherc = st.form_submit_button("Crear curso")
    if anotherc:
        if not nom_curso.strip():
            st.warning("Digite un nombre para el curso")
        else:
            st.session_state.cursos.append({
                "nombre": nom_curso.strip(),
                "tipo": tipo,
                "dur": dur,
                "grupos": [],
            })
            st.success(f"Curso '{nom_curso}' agregado.")

#Agregar grupos
if st.session_state.cursos:
    st.header("2. Agregar los grupos del curso")

    for ci, curso in enumerate(st.session_state.cursos):
        with st.expander(f"{curso['nombre']}  —  {TLABELS[curso['dur']]}  ({len(curso['grupos'])} grupo(s))", expanded=True):

            op_horario = [h for h in HORARIOS_DB if h["dur"] == curso["dur"]]
            horario_labels = [f"{h['ini']} – {h['fin']}" for h in op_horario]

            with st.form(f"form_grupo_{ci}", clear_on_submit=True):
                num_grupo = st.number_input("Número de grupo", min_value=1, step=1, key=f"num_{ci}")
                if curso["tipo"] == "2 días":
                    d_2 = st.selectbox("Días", list(D_2.keys()), key=f"par_{ci}")
                    dias_sel = D_2[d_2]
                else:
                    dia_sel = st.selectbox("Día", DIAS_SEM, key=f"dia_{ci}")
                    dias_sel = [dia_sel]

                horario_sel_label = st.selectbox("Horario", horario_labels, key=f"hor_{ci}")
                horario_sel = op_horario[horario_labels.index(horario_sel_label)]

                interes = st.slider("Interés en matricular este grupo", 1, 10, 5, key=f"int_{ci}")

                anotherg = st.form_submit_button("Agregar este grupo")

                if anotherg:
                    curso["grupos"].append({
                        "num": int(num_grupo),
                        "dias": dias_sel,
                        "horario": horario_sel,
                        "interes": interes,
                    })
                    st.success(f"Grupo {int(num_grupo)} agregado a '{curso['nombre']}'.")
                    st.rerun()

            if curso["grupos"]:
                st.write("**Grupos registrados:**")
                for g in curso["grupos"]:
                    st.write(f"- Grupo {g['num']}: {' y '.join(g['dias'])}, {g['horario']['ini']}–{g['horario']['fin']}, interés {g['interes']}/10")

            colb1, colb2 = st.columns(2)
            with colb1:
                if curso["grupos"] and st.button("Quitar último grupo", key=f"del_grupo_{ci}"):
                    curso["grupos"].pop()
                    st.rerun()
            with colb2:
                if st.button("Eliminar este curso", key=f"del_curso_{ci}"):
                    st.session_state.cursos.pop(ci)
                    st.rerun()

#Opciones para reiniciar
if st.session_state.cursos:
    if st.button("Reiniciar todo"):
        st.session_state.cursos = []
        st.rerun()

#Excel
st.header("3. Generar horario")
cready = [c for c in st.session_state.cursos if c["grupos"]]

if not cready:
    st.info("Para generar el documento excel del horario, tiene que agregar al menos un (1) curso con al menos un (1) grupo :) ")
else:
    if st.button("Generar excel con todas las combinaciones", type="primary"):
        buffer = io.BytesIO()
        cantidad = generar_excel(cready, archivo_s=buffer)
        buffer.seek(0)

        if cantidad == 0:
            st.error("Todas las combinaciones de horarios tienen al menos un choque entre cursos. Revise sus opciones o elimine un curso para generar una combinacion sin choques.")
        else:
            st.success(f"Se generaron {cantidad} combinaciones de horarios")
            st.download_button(
                label="Descargar el archivo horarios_finales.xlsx",
                data=buffer,
                file_name="horarios_finales.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
