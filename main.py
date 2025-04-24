celulas = [
    [0, 0, 0, 9, 1, 9, 0, 0, 0],
    [0, 0, 0, 0, 999, 0, 0, 0, 0],
]
vecinos_vivos = 0
for lista in range(len(celulas)):
    for item in range(len(celulas[lista])):
        if celulas[lista][item] == 1:
            index_item = celulas[lista].index(celulas[lista][item])
            print(f"INDEX DEL ITEM ACTUAL: {index_item}")
            # Check the last and next item
            siguiente_item = celulas[lista][item+1]
            anterior_item = celulas[lista][item-1]
            print(f"siguiente_item: {siguiente_item}")
            print(f"anterior_item: {anterior_item}")

            elemento_arriba = None
            elemento_abajo = None
            # if lista != 0:
                # Si hay algo arriba, entonces
            lista_abajo = celulas[lista-1]
            print(f"Lista abajo: {lista_abajo}")
            elemento_abajo = lista_abajo[index_item]
            print(f"Elemento abajo {elemento_abajo}")

            if siguiente_item == 1:
                vecinos_vivos += 1
            if anterior_item == 1:
                vecinos_vivos += 1

            # print(f"Celulas vivas de {lista[item]} => {vecinos_vivos}")
