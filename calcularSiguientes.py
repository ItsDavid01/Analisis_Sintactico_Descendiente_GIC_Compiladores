from modulos import re


def siguiente(gramatica, primeros):
    print("Calculando siguientes...")
    siguientes = {}
    for no_terminal in gramatica:

        siguientes[no_terminal] = []

    i = 0
    for no_terminal in list(gramatica.keys()):

        if i == 0:
            siguientes[no_terminal] = ["$"]

        for opcion_prod in gramatica[no_terminal]:
            A = no_terminal
            beta_can_be_epsilon = True
            for i in range(1, len(opcion_prod) + 1):
                B = opcion_prod[-i]

                if re.match(r"[A-Z]", B):

                    if i == 1:

                        if A not in siguientes[B]:
                            siguientes[B].append(A)

                        if "&" not in primeros[B]:
                            beta_can_be_epsilon = False

                    else:

                        beta = opcion_prod[-i + 1]

                        if re.match(r"[A-Z]", beta):
                            siguientes[B].extend(
                                [
                                    c
                                    for c in primeros[beta]
                                    if c != "&" and c not in siguientes[B]
                                ]
                            )
                        else:
                            if beta not in siguientes[B]:
                                siguientes[B].append(beta)

                        if beta_can_be_epsilon:
                            if A not in siguientes[B]:
                                siguientes[B].append(A)

                        if "&" not in primeros[B]:
                            beta_can_be_epsilon = False

                else:
                    beta_can_be_epsilon = False
        i += 1

    for no_terminal in list(siguientes.keys()):
        i = 0
        while i < len(siguientes[no_terminal]):
            sig = siguientes[no_terminal][i]

            if re.match(r"[A-Z]", sig):
                if sig == no_terminal:
                    siguientes[no_terminal].remove(sig)
                    i = 0
                else:
                    if no_terminal in siguientes[sig]:
                        siguientes[no_terminal].extend(
                            [
                                e
                                for e in siguientes[sig]
                                if e not in siguientes[no_terminal] and e != no_terminal
                            ]
                        )
                        siguientes[sig] = siguientes[no_terminal]
                        siguientes[no_terminal].remove(sig)
                        i = 0
                    else:
                        siguientes[no_terminal].extend(
                            [
                                e
                                for e in siguientes[sig]
                                if e not in siguientes[no_terminal]
                            ]
                        )
                        siguientes[no_terminal].remove(sig)
                        i = 0

            else:
                i += 1

    return siguientes
