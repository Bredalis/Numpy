
import numpy as np

# Matriz y propiedades
matriz = np.arange(24).reshape(4, 6)

# Propiedades
print("Propiedades:\n")
print(f"Cantidad de filas y columnas: {matriz.shape}")
print(f"Dimensión: {matriz.ndim}")
print(f"Tamaño de la matriz: {matriz.size}")

# Operaciones estadísticas
print("\nOperaciones estadísticas:")
print(f"Mayor elemento de cada fila: {np.amax(matriz, axis = 1)}")
print(f"Menor elemento de cada columna: {np.amin(matriz, axis = 0)}")
print(f"Rango de columnas: {np.ptp(matriz, axis = 0)}")
print(f"Rango de filas: {np.ptp(matriz, axis = 1)}")

# Tipos de matrices
print("\nTipos de matrices:")
print(f"Matriz de ceros:\n{np.zeros((3, 4))}")  
print(f"Matriz de unos:\n{np.ones((3, 4))}")
print(f"Matriz 1D: {np.arange(10)}")
print(f"Matriz 3D:\n{np.arange(27).reshape(3, 3, 3)}")
print(f"Matriz rápida:\n{np.linspace(99, 88, 25)}")