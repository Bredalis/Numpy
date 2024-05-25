
import numpy as np

# Matriz y propiedades

matriz = np.arange(24).reshape(4, 6)

print("Propiedades:\n")
print(f"Cantidades de filas y columnas: {matriz.shape}")
print(f"Dimension: {matriz.ndim}")
print(f"Cantidad de la matriz: {matriz.size}")

# Estadisticas

print("\nOperaciones estadisticas:")
print(f"\nMayor elemento de filas: {np.amax(matriz, 0)}")
print(f"Menor elemento de columnas: {np.amin(matriz, 1)}")

print(f"Rango de columnas: {np.ptp(matriz, axis = 1)}")
print(f"Rango de filas: {np.ptp(matriz, axis = 0)}")

# Tipos de matrices

print("\nTipos de matrices:")
print(f"\nMatriz de ceros: \n{np.zeros((3, 4))}")	
print(f"\nMatriz de unos: \n{np.ones((3, 4))}")

print(f"\nMatriz de 1D: {np.arange(10)}")
print(f"\nMatriz 3D: \n{np.arange(27).reshape(3, 3, 3)}")

print(f"\nMatriz rapida: \n{np.linspace(99, 88, 25)}")