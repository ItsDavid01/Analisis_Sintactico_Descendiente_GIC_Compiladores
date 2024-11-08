from modulos import re
from io import StringIO

from LecturaArchivoGramatica import convertir_archivo_gramatica
from recursividad import eliminar_recursividad_izquierda
from factorizacion import factorizar_izquierda
from calcularPrimeros import primero
from calcularSiguientes import siguiente
from algoritmoTablaM import generarTablaM
from AlgoritmoVerificacionCadenas import verificarCadena

import streamlit as st # para correr esta aplicacion desde su ordenador use: python -m streamlit run main.py
import pandas as pd

def procesar(archivo):
    gramatica, hasError = convertir_archivo_gramatica(archivo)
    if hasError:
        print("6")
        return gramatica, hasError, -1, -1, -1, -1
    else:
        try:
            gram_recurFree = eliminar_recursividad_izquierda(gramatica)
            clean_gramatica = factorizar_izquierda(gram_recurFree)
            try:
                prims = primero(clean_gramatica)
                try:
                    sigs = siguiente(clean_gramatica, prims)
                    try:
                        tablaM = generarTablaM(clean_gramatica, prims, sigs)
                    except:
                        print("5")
                        return gramatica, hasError, clean_gramatica, prims, sigs, -1
                except:
                    print("4")
                    return gramatica, hasError, clean_gramatica, prims, -1, -1
            except:
                print("3")
                return gramatica, hasError, clean_gramatica, -1, -1, -1
        except:
            print("2")
            return gramatica, hasError, -1, -1, -1, -1
        print("1")
        return gramatica, hasError, clean_gramatica, prims, sigs, tablaM

def escribir_gramatica(gramatica):
    if gramatica == -1:
        st.write("Hubo un error al escribir la gramática")
    else:
        cad = ""
        for no_terminal in gramatica:
            for opcion_prod in gramatica[no_terminal]:
                cad += no_terminal + "->" + "".join(opcion_prod) + "\n"
        st.text(cad)

def escribir_prim_sigs(dicc, tipo):
    if dicc == -1:
        st.write("Hubo un error al escribir la tabla")
    else:
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

    gramatica, hasError, clean_gramatica, prims, sigs, tablaM = procesar(cadena)


    st.divider()
    
    if not hasError:
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
        if isinstance(tablaM, pd.DataFrame):
            st.write(tablaM) #tablaM

            st.divider()

            st.subheader("Verificacion de Palabras")
            st.write("Escriba aqui la cadena que desea verificar...")
            cadena = st.text_input("Escriba aqui la cadena que desea verificar", value=None, placeholder="¡Escriba aqui!", help="Ejemplo: i*i+i")
            if cadena is not None:
                st.write(f"cadena ingresada: {cadena}")
                resultadoVerificacion = verificarCadena(tablaM, cadena)
                st.write(resultadoVerificacion)
        elif tablaM == -2:
            st.write("Hubo un conflicto en las celdas de la tabla M, por ende, no pudo generarse")
        elif tablaM == -1:
            st.write("Los componentes necesarios para la tabla M no pudieron generarse, por ende la tabla M tampoco")
    else:
        st.write(gramatica)


