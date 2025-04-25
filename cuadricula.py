import os
import random

# Colores (sin usar, pero preparados para futuras implementaciones)
# ROJO = "\033[31m"
# VERDE = "\033[32m"
# BLANCO = "\033[37m"

# Obtener dimensiones del terminal
dimensiones = {
    "col": os.get_terminal_size().columns,
    "lines": os.get_terminal_size().lines,
}

# Función para devolver una lista de caracteres
def contenido_caracteres():
    return ["#", "*", "@", "$", "%", "&"]

# Función para generar contenido aleatorio para la cuadrícula
def simular_contenido(ancho):
    caracteres = contenido_caracteres()
    contenido = ""
    for _ in range(ancho - 2):  # Ajustar para el ancho del borde
        contenido += random.choice(caracteres)
    return contenido

# Función para dibujar la cuadrícula
def dibujar_cuadricula(contenido):
    ancho = dimensiones["col"]
    alto = dimensiones["lines"]
    # Borde superior
    print(chr(9484) + chr(9472) * (ancho - 2) + chr(9488))
    # Filas centrales
    for _ in range(alto - 2):
        print(chr(9474) + contenido + chr(9474))
    # Borde inferior
    print(chr(9492) + chr(9472) * (ancho - 2) + chr(9496))

# Función para imprimir registros numerados
def imprimir_registros(numero_registro):
    for i in range(1, numero_registro + 1):
        print("Registro", str(i).ljust(10))

# Ejecución principal
if __name__ == "__main__":
    print(
        "Dimensiones del terminal: Contador de columnas =",
        str(dimensiones["col"]).ljust(40),
        "Contador de líneas =",
        str(dimensiones["lines"]).ljust(20),
    )
    # Generar cuadrícula con contenido aleatorio
    dibujar_cuadricula(simular_contenido(dimensiones["col"]))
    imprimir_registros(3)
