"""
Exemplo básico de funcionamento do operador bitwise (bit a bit)
em python: ~
O operador ~ (NOT) retorna 1 se o bit for 0, caso contrário
retorna 0.

Exemplo: ~10
10 = 1010
----------
-11 = 0101

Utilidade: inverter o valor de um bit.

"""

# Definimos uma variável com o valor 10
a = 10
b = ~a
print(a)
print(b)
print(bin(a))
print(bin(b))
