
import numpy as np

matriz_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Formulas estadisticas

print("Formulas estadisticas:")

print(f"\nPercentile de filas: {np.percentile(matriz_2d, 50, axis = 0)}")
print(f"Media: {np.median(matriz_2d)}")

print(f"Media Aritmetica: {np.mean(matriz_2d)}")
print(f"Promedio Ponderado: {np.average(matriz_2d)}")
print(f"Desviacion Estandar: {np.std(matriz_2d)}")

print(f"\nMatriz: \n{matriz_2d}")