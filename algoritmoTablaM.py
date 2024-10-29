from modulos import re
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
    tablaM = [["" for x in range(columnas)] for x in range(filas)]

    for no_terminal in no_terminales:

        no_terminal_index = no_terminales.index(no_terminal)

        for opcion_prod in gramatica[no_terminal]:

            alpha = opcion_prod[0]

            prim_alpha_has_epsilon = False
            if re.match(r"[A-Z]", alpha):
                for prim in primeros[alpha]:

                    if prim == "&":
                        prim_alpha_has_epsilon = True

                    else:

                        tablaM[no_terminal_index][terminales.index(prim)] = opcion_prod

                if prim_alpha_has_epsilon:

                    for sig in siguientes[no_terminal]:

                        tablaM[no_terminal_index][terminales.index(sig)] = opcion_prod

            else:
                if alpha == "&":
                    for sig in siguientes[no_terminal]:

                        tablaM[no_terminal_index][terminales.index(sig)] = opcion_prod

                else:
                    tablaM[no_terminal_index][terminales.index(alpha)] = opcion_prod

    return no_terminales, terminales, tablaM
