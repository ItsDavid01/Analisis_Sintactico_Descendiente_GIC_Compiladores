from modulos import comilla, re

def convertir_archivo_gramatica(archivo): #pasar un archivo StringIO (usado en streamlit)
    try:
        gramatica = {}
        
        for linea in archivo:
            linea_limpia = re.sub(r"[ \t\r\f\v\n]+", "", linea)
            #print(f"linea_limpia {linea_limpia}")
            if "->" in linea_limpia:
                separacion = linea_limpia.split("->")
                no_terminal = separacion[0]
                cuerpo_prod = separacion[1]
                cuerpo_prod_lista = re.findall(rf"[A-Z]{comilla}+|[a-zA-Z]|\S", cuerpo_prod)

                if no_terminal not in gramatica:
                    gramatica[no_terminal] = []

                gramatica[no_terminal].append(cuerpo_prod_lista)
            elif linea_limpia == "":
                continue
            else:
                return "Una o mas lineas del archivo de entrada no corresponden con una produccion válida", True
            
        
        return gramatica, False
    except:
        return "No se ha podido procesar la gramatica, es posible que no cumpla con la sintaxis necesaria", True


