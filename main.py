import os
import random
import time
from cuadricula import simular_contenido, dibujar_cuadricula  # Importar funciones de cuadricula.py


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
    """Imprime el tablero en la terminal usando las funciones de cuadricula.py."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola
    contenido = ""
    for fila in tablero:
        
        contenido += ''.join("█" if celda else " " for celda in fila) + "\n"
    dibujar_cuadricula(contenido)  # Usar la función de cuadricula.py para dibujar


# Configuración
filas = 50
columnas = 90
tablero = crear_tablero(filas, columnas)

# Ciclo del juego
generaciones = 50
for gen in range(generaciones):
    print(f"Generación {gen + 1}")
    imprimir_tablero(tablero)
    tablero = siguiente_generacion(tablero)
    time.sleep(0.3)  # Espera para que se note el cambio