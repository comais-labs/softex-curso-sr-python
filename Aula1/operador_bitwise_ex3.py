"""
Exemplo básico de funcionamento do operador bitwise (bit a bit)
em python: ^
O operador ^ (XOR) retorna 1 se apenas um dos bits for 1, caso contrário
retorna 0.

Exemplo: 10 ^ 11
10 = 1010
11 = 1011
----------
10 = 0001

Utilidade: verificar se apenas um bit está ligado ou desligado.

"""

# Definimos uma variável com o valor 10
a = 10
b = 11
c = a ^ b
print(c)
print(bin(a))
print(bin(b))
print(bin(c))
