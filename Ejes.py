
import numpy as np

matriz_2D = np.array([[0, 1, 2], [4, 2, 3]])
altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

union = np.stack((altura, peso), axis = 0)
separacion = np.split(union, 2)

# Mostrar datos

print("Union de altuta y peso (Columnas): \n", np.stack((altura, peso), axis = 1))
print("\nConcatenacion: \n", np.concatenate((altura, peso)))

print("\nUnion (Filas): \n", union, type(union))
print("\nSeparacion: \n", separacion, type(separacion))

print("\nSuma de filas (matriz): \n", np.sum(matriz_2D, axis = 0))	
print("\nSuma de columnas (matriz): \n", np.sum(matriz_2D, axis = 1))