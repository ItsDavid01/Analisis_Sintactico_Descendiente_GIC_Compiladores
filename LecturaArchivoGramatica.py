from modulos import comilla, re


def leer_archivo_gramatica(entrada): #para leer la gramatica pasando como parametro la url del archivo txt (solo en google colab)
    print("Leyendo archivo y procesando la entrada...")
    gramatica = {}
    with open(entrada, "r") as archivo:

        for linea in archivo:

            separacion = linea.split("->")
            no_terminal = separacion[0]
            cuerpo_prod = separacion[1].replace("\n", "")
            cuerpo_prod_lista = re.findall(rf"[A-Z]{comilla}+|[a-zA-Z]|\S", cuerpo_prod)

            if no_terminal not in gramatica:
                gramatica[no_terminal] = []

            gramatica[no_terminal].append(cuerpo_prod_lista)

    return gramatica

def convertir_archivo_gramatica(archivo): #pasar un archivo StringIO (usado en streamlit)
    gramatica = {}
    for linea in archivo:
        separacion = linea.split("->")
        no_terminal = separacion[0]
        cuerpo_prod = separacion[1].replace("\n", "")
        cuerpo_prod_lista = re.findall(rf"[A-Z]{comilla}+|[a-zA-Z]|\S", cuerpo_prod)

        if no_terminal not in gramatica:
            gramatica[no_terminal] = []

        gramatica[no_terminal].append(cuerpo_prod_lista)
    return gramatica


