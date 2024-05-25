
import numpy as np

# Mostrar datos

print(f"Random: \n{np.random.randint(10, size = (3, 3))}")
print(f"\nDecimal: \n{np.random.rand(5)}")

print("\nLista Random:\n", np.random.choice([3, 5, 7, 8, 9, 4], size = (3, 3)))
print("\nProbabilidad:", 
	np.random.choice([2, 4, 6], p = [0.5, 0.2, 0.3], size = (1)))
print(np.random.choice([2, 4, 8, 10], p = [0.3, 0.1, 0.1, 0.5], size = (50)))