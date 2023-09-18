"""
Coleções em Python:
- Dictionary: Dicionário de dicionário.
"""

# Dictionary: Família de dicionários
dict1 = {
    "filho1": { # Dicionário filho1
        "nome": "Emil",
        "ano": 2004
    },
    "filho2": { # Dicionário filho2
        "nome": "Tobias",
        "ano": 2007
    },
    "filho3": { # Dicionário filho3
        "nome": "Linus",
        "ano": 2011
    }
}

print(dict1)

# Acesso ao dicionário filho1
print(dict1["filho1"])

# Acesso aos nomes dos filhos
for x in dict1.values():
    print(x["nome"])

