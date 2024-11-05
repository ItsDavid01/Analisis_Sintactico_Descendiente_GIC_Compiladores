from modulos import re
from modulos import pd

def generarTablaM(gramatica, primeros, siguientes):
    print("Generando la tabla M...")

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

        #no_terminal_index = no_terminales.index(no_terminal)

        for opcion_prod in gramatica[no_terminal]:

            alpha = opcion_prod[0]

            prim_alpha_has_epsilon = False
            if re.match(r"[A-Z]", alpha):
                for prim in primeros[alpha]:

                    if prim == "&":
                        prim_alpha_has_epsilon = True

                    else:
                        produccion = no_terminal + "->" + "".join(opcion_prod)
                        tablaM.loc[no_terminal, prim] = produccion
                        #tablaM[no_terminal_index][terminales.index(prim)] = opcion_prod

                if prim_alpha_has_epsilon:

                    for sig in siguientes[no_terminal]:

                        produccion = no_terminal + "->" + "".join(opcion_prod)
                        tablaM.loc[no_terminal, sig] = produccion
                        #tablaM[no_terminal_index][terminales.index(sig)] = opcion_prod

            else:
                if alpha == "&":
                    for sig in siguientes[no_terminal]:

                        produccion = no_terminal + "->" + "".join(opcion_prod)
                        tablaM.loc[no_terminal, sig] = produccion
                        #tablaM[no_terminal_index][terminales.index(sig)] = opcion_prod

                else:
                    produccion = no_terminal + "->" + "".join(opcion_prod)
                    tablaM.loc[no_terminal, alpha] = produccion
                    #tablaM[no_terminal_index][terminales.index(alpha)] = opcion_prod

    return tablaM
