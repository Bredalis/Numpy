
import numpy as np

# Crear dos arrays

a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

# Concatenar los arrays a lo 
# largo del segundo eje usando np.c_

c = np.c_[a, b]

print(c)