
import numpy as np

# Definición de la matriz 2D
matriz_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Fórmulas estadísticas
print("Fórmulas estadísticas:")

print(f"\nPercentil de filas (50%): {np.percentile(matriz_2d, 50, axis = 0)}")
print(f"Mediana: {np.median(matriz_2d)}")
print(f"Media aritmética: {np.mean(matriz_2d)}")
print(f"Promedio ponderado: {np.average(matriz_2d)}")
print(f"Desviación estándar: {np.std(matriz_2d)}")

# Mostrar la matriz original
print(f"\nMatriz:\n{matriz_2d}")