from random import randint



def genera_lista(ancho, alto):
    return [0 if randint(0,1) else 1 for i in range(ancho*alto)]

def dibuja_lista(lista, ancho, alto):
     for y in range(alto):
        for x in range(ancho):
            pos = x+y * ancho
            print(lista[pos], end="")
        print()
ancho = 20
alto = 50
lista = genera_lista(ancho, alto)
dibuja_lista(lista, ancho, alto)  
