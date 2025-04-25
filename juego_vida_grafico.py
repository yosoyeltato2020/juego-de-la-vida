
import pygame 
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


def imprimir_tablero(tablero, pantalla, tam_celda):
    pantalla.fill((0, 0, 0))  
    filas = len(tablero)
    columnas = len(tablero[0])
    for i in range(filas): 
        for j in range(columnas):  
            if tablero[i][j] == 1:  
                color = (0, 255, 0)  
            else: 
                color = (0, 0, 0)  
            rect = pygame.Rect(j * tam_celda, i * tam_celda, tam_celda, tam_celda) 
            pygame.draw.rect(pantalla, color, rect)  
    pygame.display.flip()  


filas = 20 
columnas = 40  
tam_celda = 20  
ancho_pantalla = columnas * tam_celda  
alto_pantalla = filas * tam_celda  


tablero = crear_tablero(filas, columnas) 
pantalla = pygame.display.set_mode((ancho_pantalla, alto_pantalla))  
pygame.display.set_caption("Juego de la Vida") 
reloj = pygame.time.Clock()  


generaciones = 100  
for gen in range(generaciones): 
    for evento in pygame.event.get():  
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
    imprimir_tablero(tablero, pantalla, tam_celda) 
    tablero = siguiente_generacion(tablero)  
    reloj.tick(3)  
