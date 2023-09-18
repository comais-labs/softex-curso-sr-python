"""
Exemplo básico de pacotes úteis NumPy
Manipulação de Formas: Numpy oferece várias
maneiras de alterar a forma dos arrays sem 
alterar seus dados. Isso inclui o reshape 
de arrays e a transposição de matrizes.
"""
import numpy as np

a = np.array([[1,2,3],[4,5,6]])
b = a.reshape(3, 2)   # altera a forma de a para 3x2
c = a.T               # transpõe a matriz a

print("a: ")
print(a)
print("b: ")
print(b)
print("c: ")
print(c)
