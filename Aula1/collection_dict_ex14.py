"""
Coleções em Python:
- Dictionary: Removendo o último item inserido no dicionário utilizando pipitem().
"""

# Dictionary: Definindo um dicionário
dict1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

# Dictionary: Removendo o último item inserido no dicionário utilizando pipitem()
dict1.popitem()
print(dict1)
