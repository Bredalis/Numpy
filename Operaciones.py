
import numpy as np

# Matrices
matriz_1 = np.arange(24).reshape(4, 6)
matriz_2 = np.array([[2, 3, 4, 5, 6, 7]])
matriz_1d = np.array([90, 7, 9, 4, 2, 1])

# Elaboraciones
print(f"Posición de elemento (matriz_1[3, 4]): {matriz_1[3, 4]}")
print(f"Concatenación de matrices:\n{np.concatenate((matriz_1, matriz_2), axis = 0)}")
print(f"\nElementos de matriz_2 >= 4:\n{np.array(matriz_2 >= 4)}")

# Métodos
print(f"\nPotencia de elementos en matriz_1d:\n{np.power(matriz_1d, 2)}")
print(f"\nOrdenamiento de matriz_1d:\n{np.sort(matriz_1d)}")

print(f"\nMáximo de matriz_2: {matriz_2.max()}")
print(f"Mínimo de matriz_2: {matriz_2.min()}")

# Operaciones básicas
print(f"\nSuma de matrices:\n{np.add(matriz_1, matriz_2)}")
print(f"\nResta de matrices:\n{np.subtract(matriz_1, matriz_2)}")
print(f"\nMultiplicación de matrices:\n{np.multiply(matriz_1, matriz_2)}")
print(f"\nDivisión de matrices:\n{np.divide(matriz_1, matriz_2)}")

# Mostrar matrices originales
print(f"\nMatriz 1:\n{matriz_1}")
print(f"\nMatriz 2: {matriz_2}")