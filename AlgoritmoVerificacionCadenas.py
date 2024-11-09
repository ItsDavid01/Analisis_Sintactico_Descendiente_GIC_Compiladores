from modulos import copy
from modulos import pd
from modulos import re
from modulos import comilla

def verificarCadena(tablaM, cad):
    pila = ["$", tablaM.index[0]]  # inicialmente tendra un signo $ y el simbolo no terminal de inicio
    cadena = list(cad + "$")

    tabla = {"pila": [], "cadena": [], "accion": []}  # generar la tabla, luego se va a convertir en un dataframe
    #print("INICIO")
    #print(f"pila: {pila}")
    #print(f"cadena: {cadena}")

    X = pila[-1]
    #print(f"X inicial: {X}")

    while X != "$":
        X = pila[-1]
        ae = cadena[0]
        if ae not in list(tablaM.columns):
            tabla["pila"].append("".join(pila))
            tabla["cadena"].append("".join(cadena))
            tabla["accion"].append("RECHAZAR")
            return pd.DataFrame(tabla)
        #print(f"X: {X}")
        #print(f"ae: {ae}")

        if re.match(r"[A-Z]", X):  # X es un no terminal
            #print(f"X es un no terminal")
            produccion = tablaM.loc[X, ae]
            #print(f"produccion de la tablaM: {produccion}")
            if produccion != "":
                prod = produccion.split("->")
                cuerpo = re.findall(rf"[A-Z]{comilla}+|[a-zA-Z]|\S", prod[1])
                reemplazo = cuerpo[::-1]
                #print(f"reemplazo: {reemplazo}")

                tabla["pila"].append("".join(pila))
                tabla["cadena"].append("".join(cadena))
                tabla["accion"].append(produccion)
                #print(f"tabla modificada: {tabla}")
                pila.pop()
                if reemplazo != ["&"]:
                    pila.extend(reemplazo)
                #print(f"pila modificada: {pila}")

            else:
                tabla["pila"].append("".join(pila))
                tabla["cadena"].append("".join(cadena))
                tabla["accion"].append("RECHAZAR")
                break
        else:  # X es un terminal
            if X == ae:  # son iguales
                tabla["pila"].append("".join(pila))
                tabla["cadena"].append("".join(cadena))
                tabla["accion"].append("")
                #print(f"tabla modificada: {tabla}")
                pila.pop()
                cadena.pop(0)
                #print(f"pila modificada: {pila}")
                #print(f"cadena modificada: {cadena}")
            else:
                tabla["pila"].append("".join(pila))
                tabla["cadena"].append("".join(cadena))
                tabla["accion"].append("RECHAZAR")
                break

            if (X=="$") and (ae == "$"):
                #tabla["pila"].append("".join(pila))
                #tabla["cadena"].append("".join(cadena))
                tabla["accion"][-1] = "ACEPTAR"
    return pd.DataFrame(tabla)
