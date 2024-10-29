from modulos import re
from io import StringIO

from LecturaArchivoGramatica import convertir_archivo_gramatica
from recursividad import eliminar_recursividad_izquierda
from factorizacion import factorizar_izquierda
from calcularPrimeros import primero
from calcularSiguientes import siguiente
from algoritmoTablaM import generarTablaM



import streamlit as st # Use: "python -m streamlit run client_app.py" para correr esta aplicacion

def procesar(archivo):
    gramatica = convertir_archivo_gramatica(archivo)
    gram_recurFree = eliminar_recursividad_izquierda(gramatica)
    clean_gramatica = factorizar_izquierda(gram_recurFree)
    prims = primero(clean_gramatica)
    sigs = siguiente(clean_gramatica, prims)
    noterms, terms, tablaM = generarTablaM(clean_gramatica, prims, sigs)
    return gramatica, clean_gramatica, prims, sigs, tablaM

st.title("Analizador Sintactico Descendiente")
st.write("")
archivo_gramatica = st.file_uploader("Agregue el archivo txt con la gramatica")

if archivo_gramatica is not None:
    

    cadena = StringIO(archivo_gramatica.getvalue().decode("utf-8"))
    gramatica = convertir_archivo_gramatica(cadena)

    st.write(gramatica)