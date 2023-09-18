"""
Coleções em Python:
- Dictionary: Percorrendo um dicionário com o método items().
"""

# Dictionary: Definindo um dicionário
dict1 = {
    "marca": "Ford",
    "modelo": "Mustang",
    "ano": 1964,
}

# Dictionary: Percorrendo um dicionário com o método items()
for chave, valor in dict1.items():
    print(chave, valor)
    
# Exemplo para Não ³ alterar o tamanho do dicionário durante a iteração
for x, y in dict1.items():
    print(x, y)
    dict1['nova_key'] = 10
