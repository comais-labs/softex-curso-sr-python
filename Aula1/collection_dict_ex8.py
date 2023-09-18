"""
Coleções em Python:
- Dictionary: Verificando se uma chave existe no dicionário utilizando o método key().
"""

# Dictionary: Definindo um dicionário
dict1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964
}

# Dictionary: Verificando se uma chave existe no dicionário utilizando o método key()
if "modelo" in dict1.keys():
    print("Sim, 'modelo' é uma das chaves do dicionário dict1")
else:
    print("Não, 'modelo' não é uma das chaves do dicionário dict1")
    