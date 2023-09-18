"""
Coleções em Python:
- Listas: Removendo elementos de uma lista
"""

# Listas: Definindo uma lista
lista = ["banana", "maçã", "uva", "abacaxi", "laranja", "melancia"]

# Listas: Removendo elementos de uma lista
lista.remove("uva")
print(lista)

# Listas: Removendo elementos de uma lista
lista.pop(0)
print(lista)

# Listas: Removendo elementos de uma lista
del lista[0]
print(lista)

# Listas: Limpando uma lista
lista.clear()
print(lista)

# Sugestão de teste: tente remover um elemento que não existe na lista.
