from modulos import re
from io import StringIO

from LecturaArchivoGramatica import convertir_archivo_gramatica
from recursividad import eliminar_recursividad_izquierda
from factorizacion import factorizar_izquierda
from calcularPrimeros import primero
from calcularSiguientes import siguiente
from algoritmoTablaM import generarTablaM

import streamlit as st # Use: "python -m streamlit run main.py" para correr esta aplicacion
import pandas as pd

def procesar(archivo):
    gramatica = convertir_archivo_gramatica(archivo)
    gram_recurFree = eliminar_recursividad_izquierda(gramatica)
    clean_gramatica = factorizar_izquierda(gram_recurFree)
    prims = primero(clean_gramatica)
    sigs = siguiente(clean_gramatica, prims)
    noterms, terms, tablaM = generarTablaM(clean_gramatica, prims, sigs)
    return gramatica, clean_gramatica, prims, sigs, tablaM, noterms, terms

def escribir_gramatica(gramatica):
    cad = ""
    for no_terminal in gramatica:
        for opcion_prod in gramatica[no_terminal]:
            cad += no_terminal + "->" + "".join(opcion_prod) + "\n"
    st.text(cad)

def escribir_prim_sigs(dicc, tipo):
    cad = ""
    sep = ","
    for no_terminal in dicc:
        cad += f"{tipo}({no_terminal}) = [{ sep.join(dicc[no_terminal])}]\n"
    st.text(cad)


st.title("Analizador Sintactico Descendiente")
st.write("Ingrese el archivo txt con la gramatica para comenzar")
st.write("Este algoritmo realizará todos los pasos necesarios hasta llegar a la tabla M de la gramatica ingresada")
archivo_gramatica = st.file_uploader("Agregue el archivo txt con la gramatica", "txt")

if archivo_gramatica is not None:
    cadena = StringIO(archivo_gramatica.getvalue().decode("utf-8"))
    gramatica, clean_gramatica, prims, sigs, tablaM, noterms, terms = procesar(cadena)

    st.divider()

    gram_original, gram_clean = st.columns(2)

    with gram_original:
        st.subheader("Gramatica original")
        escribir_gramatica(gramatica)

    with gram_clean:
        st.subheader("Gramatica limpia")
        escribir_gramatica(clean_gramatica)

    st.divider()

    primsTab, sigsTab = st.columns(2)

    with primsTab:
        st.subheader("Tabla de Primeros")
        escribir_prim_sigs(prims, "Primero")

    with sigsTab:
        st.subheader("Tabla de Siguientes")
        escribir_prim_sigs(sigs, "Siguiente")
    
    st.divider()

    st.subheader("Tabla M")

    
    tablaMod = [[str(celda) for celda in fila] for fila in tablaM]
    st.write(pd.DataFrame(tablaMod, columns=terms, index=noterms ))
