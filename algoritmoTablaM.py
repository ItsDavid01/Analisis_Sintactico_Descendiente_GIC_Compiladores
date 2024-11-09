from modulos import re
from modulos import pd

def generarTablaM(gramatica, primeros, siguientes):
    #print("Generando la tabla M...")

    no_terminales = list(gramatica.keys())
    terminales = []
    for no_terminal in gramatica:
        for opcion_prod in gramatica[no_terminal]:
            for simbolo in opcion_prod:
                if re.match(r"[A-Z]", simbolo):
                    continue
                else:
                    if simbolo not in terminales and simbolo != "&":
                        terminales.append(simbolo)
    terminales.append("$")

    filas = len(gramatica)
    columnas = len(terminales)
    tablaM = pd.DataFrame("", columns=terminales, index=no_terminales)
    

    for no_terminal in no_terminales:

        #contador = 0
        for opcion_prod in gramatica[no_terminal]:

            prim_alpha_has_epsilon = False

            for alpha in opcion_prod:

                prim_alpha_has_epsilon = False

                if re.match(r"[A-Z]", alpha): #no terminal
                    for prim in primeros[alpha]:

                        if prim == "&":
                            prim_alpha_has_epsilon = True

                        else:
                            produccion = no_terminal + "->" + "".join(opcion_prod)
                            if tablaM.loc[no_terminal, prim] == "" or tablaM.loc[no_terminal, prim] == produccion:
                                tablaM.loc[no_terminal, prim] = produccion
                            else:
                                return -2
                            

                    if prim_alpha_has_epsilon:
                        continue
                    else:
                        break

                else:
                    if alpha == "&":
                        for sig in siguientes[no_terminal]:

                            produccion = no_terminal + "->" + "".join(opcion_prod)
                            if tablaM.loc[no_terminal, sig] == "" or tablaM.loc[no_terminal, sig] == produccion:
                                tablaM.loc[no_terminal, sig] = produccion
                            else:
                                return -2

                    else:
                        produccion = no_terminal + "->" + "".join(opcion_prod)
                        if tablaM.loc[no_terminal, alpha] == "" or tablaM.loc[no_terminal, alpha] == produccion:
                            tablaM.loc[no_terminal, alpha] = produccion
                        else:
                            return -2
                    break

            if prim_alpha_has_epsilon:
                for sig in siguientes[no_terminal]:

                    produccion = no_terminal + "->" + "".join(opcion_prod)
                    if tablaM.loc[no_terminal, sig] == "" or tablaM.loc[no_terminal, sig] == produccion:
                        tablaM.loc[no_terminal, sig] = produccion
                    else:
                        return -2

    return tablaM
