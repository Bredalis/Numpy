
import numpy as np

# Definición de arrays
altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

# Unión de altura y peso (columnas)
union = np.stack((altura, peso), axis = 0)

# Separación de la unión en dos partes
separacion = np.split(union, 2)

# Mostrar datos
print("Unión de altura y peso (columnas):\n", 
	np.stack((altura, peso), axis = 1))
print("\nConcatenación:\n", np.concatenate((altura, peso)))

print("\nUnión (filas):\n", union, type(union))
print("\nSeparación:\n", separacion, type(separacion))

# Suma de filas y columnas de la matriz 2D
matriz_2D = np.array([[0, 1, 2], [4, 2, 3]])
print("\nSuma de filas (matriz):\n", np.sum(matriz_2D, axis = 0))	
print("\nSuma de columnas (matriz):\n", np.sum(matriz_2D, axis = 1))