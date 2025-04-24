import random
import tkinter as tk


def crear_tablero(filas, columnas):
    return [[random.choice([0, 1]) for _ in range(columnas)] 
            for _ in range(filas)]


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


class JuegoVida:
    def __init__(self, master):
        self.master = master
        self.tamano_celda = 20  # Tamaño de cada celda en píxeles
        self.intervalo = 200  # Intervalo en milisegundos
        self.filas = 20
        self.columnas = 40
        self.canvas = tk.Canvas(master, width=self.columnas * 
                                self.tamano_celda, 
                                height=self.filas * 
                                self.tamano_celda, bg="white")
        self.canvas.pack()
        self.tablero = crear_tablero(self.filas, self.columnas)
        self.actualizar()

    def dibujar_tablero(self):
        self.canvas.delete("all")
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero[i][j]:
                    x1 = j * self.tamano_celda
                    y1 = i * self.tamano_celda
                    x2 = x1 + self.tamano_celda
                    y2 = y1 + self.tamano_celda
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")

    def actualizar(self):
        self.dibujar_tablero()
        self.tablero = siguiente_generacion(self.tablero)
        self.master.after(self.intervalo, self.actualizar)


# Crear ventana
ventana = tk.Tk()
ventana.title("Juego de la Vida")
juego = JuegoVida(ventana)
ventana.mainloop()
