from modulos import copy


def eliminar_recursividad_izquierda(gramatica):
  
    print("Eliminando recursividad izquierda...")

    new_gramatica = {}
    for no_terminal in list(gramatica.keys()):

        lista_alpha = []
        lista_beta = []

        for opcion_prod in gramatica[no_terminal]:

            if opcion_prod[0] == no_terminal:
                lista_alpha.append(copy.copy(opcion_prod[1:]))

            else:
                lista_beta.append(copy.copy(opcion_prod))

        new_gramatica[no_terminal] = []

        if lista_alpha:

            if lista_beta:
                for opcion_beta in lista_beta:
                    temp_beta = copy.copy(opcion_beta)
                    temp_beta.append(f"{no_terminal}'")
                    new_gramatica[no_terminal].append(copy.copy(temp_beta))
            else:
                new_gramatica[no_terminal].append([f"{no_terminal}'"])

            new_gramatica[f"{no_terminal}'"] = []

            for opcion_alpha in lista_alpha:
                temp_alpha = copy.copy(opcion_alpha)
                temp_alpha.append(f"{no_terminal}'")
                new_gramatica[f"{no_terminal}'"].append(copy.copy(temp_alpha))

            new_gramatica[f"{no_terminal}'"].append(["&"])

        else:
            new_gramatica[no_terminal] = lista_beta

    return new_gramatica
    
