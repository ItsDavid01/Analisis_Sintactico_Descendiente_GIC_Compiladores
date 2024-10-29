from modulos import copy, comilla, re


def factorizar(no_terminal, cuerpo_prod, cant):
    for i in range(1, max(len(opcion_prod) for opcion_prod in cuerpo_prod) + 1):

        if i == 1:
            patronPrev = []  # vacio en la 1 interacion
            patron = []
            for opcion_prod in cuerpo_prod:
                if opcion_prod[:i] not in patron:
                    patron.append(copy.copy(opcion_prod[:i]))

            if len(patron) == len(cuerpo_prod):
                return [], [], cuerpo_prod  ##
                break
            else:
                continue
        else:
            patronPrev = copy.copy(patron)
            patron = []
            for opcion_prod in cuerpo_prod:
                if opcion_prod[:i] not in patron:
                    patron.append(copy.copy(opcion_prod[:i]))

            if len(patron) == len(patronPrev):
                continue
            else:

                no_terminals = []
                respuesta = []
                original = []
                canti = cant
                for pat in patronPrev:
                    resPat = []
                    for opcion_prod in cuerpo_prod:
                        if opcion_prod[: len(pat)] == pat:
                            if opcion_prod[len(pat) :] == []:
                                resPat.append(["&"])
                            else:
                                resPat.append(copy.copy(opcion_prod[len(pat) :]))

                    if resPat == [["&"]]:
                        original.append(copy.copy(pat))
                    else:
                        patt = copy.copy(pat)
                        patt.append(f"{no_terminal}{comilla*canti}")
                        original.append(copy.copy(patt))
                        no_terminals.append(f"{no_terminal}{comilla*canti}")
                        respuesta.append(copy.copy(resPat))
                        canti += 1
                return no_terminals, respuesta, original


def factorizar_izquierda(gramatica):
    print("Factorizando la gramatica...")
    queue = []
    new_gramatica = {}
    for no_terminal in list(gramatica.keys()):

        queue.append(no_terminal)
        while queue:

            no_term = queue.pop(0)

            cadNoTerm = "".join(list(gramatica.keys()))

            cantComillas = len(re.findall(rf"{no_term}", cadNoTerm))

            no_terms, cuerpo_prod, original = factorizar(
                no_term, gramatica[no_term], cantComillas
            )
            new_gramatica[no_term] = copy.copy(original)

            for i in range(len(no_terms)):
                gramatica[no_terms[i]] = copy.copy(cuerpo_prod[i])

                queue.append(no_terms[i])
    return new_gramatica
