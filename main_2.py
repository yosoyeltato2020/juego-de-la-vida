import random
import os
import time


def crear_tablero(filas, columnas):
    return [[random.choice([0, 1]) for _ in range(columnas)] for _ in range(filas)]


def contar_vecinas_vivas(tablero, x, y):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinas = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0),  (1, 1)
    ]
    
    vivas = 0
    for dx, dy in vecinas:
        nx, ny = x + dx, y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            vivas += tablero[nx][ny]
    return vivas


def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    
    for i in range(filas):
        for j in range(columnas):
            vivas = contar_vecinas_vivas(tablero, i, j)
            if tablero[i][j] == 1:
                if vivas in [2, 3]:
                    nuevo_tablero[i][j] = 1
            else:
                if vivas == 3:
                    nuevo_tablero[i][j] = 1
    return nuevo_tablero


def imprimir_tablero(tablero):
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola
    for fila in tablero:
        print(' '.join("1" if celda else "0" for celda in fila))


# configuración
filas = 20
columnas = 40
tablero = crear_tablero(filas, columnas)

# ciclo del juego
generaciones = 100
for gen in range(generaciones):
    print(f"Generación {gen + 1}")
    imprimir_tablero(tablero)
    tablero = siguiente_generacion(tablero)
    time.sleep(0.3)  # Espera para que se note el cambio
