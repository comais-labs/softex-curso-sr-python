"""
Exemplo básico de funcionamento do operador bitwise (bit a bit)
em python: >>
O operador >> (rigth shift) desloca os bits para a direita.

Exemplo: 10 >> 2
10 = 1010
----------
2 = 10

Utilidade: inverter o valor de um bit.

"""

# Definimos uma variável com o valor 10
a = 10
b = a >> 2
print(a)
print(b)
print(bin(a))
print(bin(b))
