"""
Coleções em Python:
- Dictionary: Percorrendo um dicionário com o loop for.
"""

# Dictionary: Definindo um dicionário
dict1 = {
    "marca": "Ford",
    "ano": 1964,
    "modelo": "Mustang",
}

# Dictionary: Percorrendo um dicionário com o loop for (imprimindo as chaves)
for x in dict1:
    print(x)
    dict1[x] = "Valor unico" #dá erro se mudar o temanho dict durante iteração

# Dictionary: Percorrendo um dicionário com o loop for (imprimindo os valores)
for x in dict1:
    print(f"chave: {x}, valor: {dict1[x]}")

