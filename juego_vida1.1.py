import random  
import os      

def crear_tablero(filas, columnas):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.choice([0, 1]))  
        tablero.append(fila) 
    return tablero

def contar_vecinas_vivas(tablero, x, y):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    
    posiciones_vecinas = []
    for dx, dy in vecinas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            posiciones_vecinas.append((nx, ny))
    
    vivas = 0
    for nx, ny in posiciones_vecinas:
        vivas += tablero[nx][ny]
    
    return vivas



def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            vivas = contar_vecinas_vivas(tablero, i, j)
            if tablero[i][j] == 1:  # Celda viva
                if vivas in [2, 3]:
                    nuevo_tablero[i][j] = 1  # Sobrevive
            else:  # Celda muerta
                if vivas == 3:
                    nuevo_tablero[i][j] = 1  # Nace una nueva célula
    return nuevo_tablero

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(str(celda) for celda in fila))

# configuración del tablero
filas = 10
columnas = 20
tablero = crear_tablero(filas, columnas)

# cuando es el fin del juego e imprimir el tablero
generaciones = 3
for gen in range(generaciones):
    print(f"Generación {gen + 1}:")
    imprimir_tablero(tablero)
    input("Presiona Enter para ver como crece la siguiente generación...")
    tablero = siguiente_generacion(tablero)
    print()