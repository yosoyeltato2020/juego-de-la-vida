celulas = [
    [0, 0, 0, 0, 1, 1, 0, 0, 0],
    [2, 0, 0, 1, 1, 1, 0, 0, 1],
    [3, 0, 0, 6, 7, 8, 0, 0, 1],
]

for lista in range(len(celulas)-1):
    # print(celulas[lista])
    for item in range(len(celulas[lista])-1):
        vecinos_vivos = 0
        if celulas[lista][item] == 1:
            print(celulas[lista])
            index_item = celulas[lista].index(celulas[lista][item])
            # Check the last and next item
            siguiente_item = celulas[lista][item+1]
            anterior_item = celulas[lista][item-1]

            lista_abajo = celulas[lista+1]
            elemento_abajo = lista_abajo[index_item]
            elemento_abajo_derecha = lista_abajo[index_item+1]
            elemento_abajo_izquierda = lista_abajo[index_item-1]

            if siguiente_item == 1:
                vecinos_vivos += 1
            if anterior_item == 1:
                vecinos_vivos += 1
            if elemento_abajo == 1:
                vecinos_vivos += 1
            if elemento_abajo_izquierda == 1:
                vecinos_vivos += 1
            if elemento_abajo_derecha == 1:
                vecinos_vivos += 1

            print(f"VECINOS VIVOS => {vecinos_vivos}")
            print()
            print()
            print()
