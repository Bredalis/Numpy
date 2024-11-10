
import numpy as np

matriz = np.array([[10, 20, 30], [40, 50, 60]])

print(f"Matriz original:\n{matriz}")
print(f"\nMatriz diagonal:\n{np.diag(matriz)}")
print("\nMatriz de identidad:\n", np.eye(3))