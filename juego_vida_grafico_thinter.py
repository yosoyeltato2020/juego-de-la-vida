import tkinter as tk
import random

def crear_tablero(filas, columnas):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            celda = random.choice([0, 1])
            fila.append(celda)
        tablero.append(fila)
    return tablero

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
        nx = x + dx
        ny = y + dy
        if 0 <= nx < filas and 0 <= ny < columnas:
            vivas += tablero[nx][ny]
    return vivas

def siguiente_generacion(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = []
    for i in range(filas):
        nueva_fila = []
        for j in range(columnas):
            vivas = contar_vecinas_vivas(tablero, i, j)
            if tablero[i][j] == 1:
                if vivas in [2, 3]:
                    nueva_fila.append(1)
                else:
                    nueva_fila.append(0)
            else:
                if vivas == 3:
                    nueva_fila.append(1)
                else:
                    nueva_fila.append(0)
        nuevo_tablero.append(nueva_fila)
    return nuevo_tablero

def imprimir_tablero(tablero, canvas, tam_celda):
    filas = len(tablero)
    columnas = len(tablero[0])
    for i in range(filas):
        for j in range(columnas):
            color = "green" if tablero[i][j] == 1 else "black"
            x1, y1 = j * tam_celda, i * tam_celda
            x2, y2 = x1 + tam_celda, y1 + tam_celda
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

filas = 20
columnas = 40
tam_celda = 20

tablero = crear_tablero(filas, columnas)

ventana = tk.Tk()
ventana.title("Juego de la Vida")
canvas = tk.Canvas(ventana, width=columnas * tam_celda, height=filas * tam_celda, bg="white")
canvas.pack()

def actualizar():
    global tablero
    tablero = siguiente_generacion(tablero)
    canvas.delete("all")
    imprimir_tablero(tablero, canvas, tam_celda)
    ventana.after(300, actualizar)

imprimir_tablero(tablero, canvas, tam_celda)
ventana.after(300, actualizar)
ventana.mainloop()
