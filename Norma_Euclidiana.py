
# Librerías

import numpy as np
import numpy.linalg as LA
import math

vector = np.array([2, 5])

# Crear formula

def norma_vector(vector):

	cuadrados = [elemento ** 2 for elemento in vector]
	print(f"|| {vector} || = {math.sqrt(sum(cuadrados))}")

norma_vector(vector)

# Usar la formula de numpy

print(LA.norm(vector))