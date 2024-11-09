from modulos import re, copy


def primero(gramatica):
    #print("Calculando primeros...")
    primeros = {}
    tabla = {}

    search_table = False

    for no_terminal in list(gramatica.keys()):

        primeros[no_terminal] = []
        tabla[no_terminal] = []
        cont = 0

        for opcion_prod in gramatica[no_terminal]:

            if re.match(r"[A-Z]", opcion_prod[0]):

                if opcion_prod[0] not in primeros[no_terminal]:

                    primeros[no_terminal].append(opcion_prod[0])
                    tabla[no_terminal].append([opcion_prod[0], cont, 0])

                    search_table = True

            else:

                if opcion_prod[0] not in primeros[no_terminal]:

                    primeros[no_terminal].append(opcion_prod[0])

            cont += 1

    for no_terminal in list(gramatica.keys()):

        for prim in primeros[no_terminal]:

            if re.match(r"[A-Z]", prim):

                primeros[no_terminal].extend(
                    [
                        e
                        for e in primeros[prim]
                        if e not in primeros[no_terminal] and e != "&"
                    ]
                )

            else:

                continue

    while search_table:

        search_table = False

        for no_terminal in list(tabla.keys()):

            i = 0

            while i < len(tabla[no_terminal]):

                caso = tabla[no_terminal][i]

                if "&" in primeros[caso[0]]:

                    primeros[no_terminal].extend(
                        [
                            e
                            for e in primeros[caso[0]]
                            if e not in primeros[no_terminal] and e != "&"
                        ]
                    )

                    primeros[no_terminal].remove(caso[0])

                    nextlist = copy.copy(
                        gramatica[no_terminal][caso[1]][caso[2] + 1 : caso[2] + 2]
                    )

                    if nextlist:

                        next = nextlist[0]

                        if re.match(r"[A-Z]", next):

                            primeros[no_terminal].append(next)

                            caso[0] = next
                            caso[2] += 1
                            i = 0

                        else:

                            primeros[no_terminal].append(next)

                            tabla[no_terminal].remove(caso)

                            i = 0

                    else:

                        primeros[no_terminal].append("&")

                        tabla[no_terminal].remove(caso)

                        i = 0

                else:

                    has_noterm = False

                    for prim in primeros[caso[0]]:

                        if re.match(r"[A-Z]", prim):

                            has_noterm = True

                            break

                    if has_noterm:

                        i += 1

                        search_table = True

                    else:

                        tabla[no_terminal].remove(caso)

                        primeros[no_terminal].remove(caso[0])

                        i = 0

    for no_terminal in primeros:

        i = 0

        while i < len(primeros[no_terminal]):
            prim = primeros[no_terminal][i]

            if re.match(r"[A-Z]", prim):

                primeros[no_terminal].extend(
                    [
                        e
                        for e in primeros[prim]
                        if e not in primeros[no_terminal] and e != "&"
                    ]
                )

                primeros[no_terminal].remove(prim)

                i = 0

            else:

                i += 1

    return primeros
