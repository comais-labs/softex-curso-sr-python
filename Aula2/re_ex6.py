import re

# Definindo o texto
text = "Conforme Art. 5 da constituição..."

# Definindo o dicionário de substituições
substitutions = {
    "Art.": "Artigo",
    # Adicione outras substituições aqui
}

# Substituindo todas as abreviações
for to_replace, replacement in substitutions.items():
    # Escape dos metacaracteres no termo a ser substituído
    pattern = re.escape(to_replace)
    text = re.sub(pattern, replacement, text)

# Imprimindo o texto
print(text)
