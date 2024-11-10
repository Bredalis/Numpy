
import numpy as np

# Crear y concatenar dos arrays a lo largo del segundo eje
a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])
concatenacion = np.c_[a, b]

print(concatenacion)