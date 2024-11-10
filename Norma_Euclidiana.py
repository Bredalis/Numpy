
import numpy as np
import numpy.linalg as LA
import math

vector = np.array([2, 5])

# Crear fórmula personalizada
def norma_vector(vector):
    cuadrados = np.square(vector)  # Usar la función numpy para simplificar
    print(f"|| {vector} || = {math.sqrt(np.sum(cuadrados))}")

# Mostrar la norma usando la fórmula personalizada
norma_vector(vector)

# Usar la fórmula de numpy
print(LA.norm(vector))