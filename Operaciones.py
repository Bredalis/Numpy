
import numpy as np

# Matrices

matriz_1 = np.arange(24).reshape(4, 6)
matriz_2 = np.array([[2, 3, 4, 5, 6, 7]])
matriz_1d = np.array([90, 7, 9, 4, 2, 1])

# Elaboraciones

print(f"Posicion de elemento: {matriz_1[3, 4]}")
print(f"\nConcatenacion: \n {np.concatenate((matriz_1, matriz_2))}")
print(np.array(matriz_2 >= 4))

# Metodos

print(f"\nPotencia: {np.power(matriz_1d, 2)}")
print(np.sort(matriz_1d))

print(f"\nMaximo: {matriz_2.max()} \n Minimo: {np.array(matriz_2.min())}")

# Operaciones Basicas

print(f"\nSuma: \n {np.add(matriz_1, matriz_2)}")
print(f"\nResta: \n {np.subtract(matriz_1, matriz_2)}")
print(f"\nMultiplicacion: \n {np.multiply(matriz_1, matriz_2)}")
print(f"\nDivision: \n {np.divide(matriz_1, matriz_2)}")

print(f"\nMatriz 1: \n{matriz_1} \nMatriz 2: {matriz_2}")