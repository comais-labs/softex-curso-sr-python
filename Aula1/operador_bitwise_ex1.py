"""
Exemplo básico de funcionamento do operador bitwise (bit a bit)
em python: &
O operador & (and) retorna 1 se ambos os bits forem 1, caso contrário
retorna 0.

Exemplo: 10 & 10
10 = 1010
10 = 1010
----------
10 = 1010

Utilidade: verificar se um bit está ligado ou desligado.

"""

# Definimos uma variável com o valor 10
a = 10
b = 10
c = a & b
print(c)
print(bin(a))
print(bin(b))
print(bin(c))
