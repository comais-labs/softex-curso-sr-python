"""
Exemplo básico de pacotes úteis NumPy
Broadcasting: Broadcasting é a maneira que Numpy 
tem de realizar operações matemáticas entre arrays 
de diferentes formas. É um recurso poderoso que 
permite que você faça isso de uma maneira que 
normalmente exigiria loops.
"""
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[0, 1, 2],[3,4,5],[6,7,8]])
c = a + b          # o array a é 'broadcast' para coincidir com a forma de b

print("a: ", a)
print("b: " , b)
print("-------")
print("c: ", c)
