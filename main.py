from LecturaArchivoGramatica import leer_archivo_gramatica
from recursividad import eliminar_recursividad_izquierda
from factorizacion import factorizar_izquierda
from calcularPrimeros import primero
from calcularSiguientes import siguiente
from algoritmoTablaM import generarTablaM




def procesar(entrada):
    gramatica = leer_archivo_gramatica(entrada)
    gram_recurFree = eliminar_recursividad_izquierda(gramatica)
    clean_gramatica = factorizar_izquierda(gram_recurFree)
    prims = primero(clean_gramatica)
    sigs = siguiente(clean_gramatica, prims)
    noterms, terms, tablaM = generarTablaM(clean_gramatica, prims, sigs)
    return gramatica, clean_gramatica, prims, sigs, tablaM


gramatica, clean_gramatica, prims, sigs, tablaM = procesar("Ejemplo_entrada.txt")
