# Exemplo básico de pacotes úteis NumPy
# Operações Matemáticas

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b          # soma elemento a elemento
d = np.dot(a, b)   # produto escalar

print("c = a + b")
print("a: ", a)
print("b: " , b)
print("-------")
print("c: ", c)

print(f"\nProduto escalar: {d}")
