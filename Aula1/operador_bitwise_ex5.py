"""
Exemplo básico de funcionamento do operador bitwise (bit a bit)
em python: <<
O operador << (left shift) desloca os bits para a esquerda.

Exemplo: 10 << 1
10 = 1010
----------
20 = 10100

Utilidade: inverter o valor de um bit.

"""

# Definimos uma variável com o valor 10
a = 10
b = a << 1
print(a)
print(b)
print(bin(a))
print(bin(b))
