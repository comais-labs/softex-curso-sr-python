import re  # Importa o módulo de expressões regulares

# Definindo uma string
text = "O gato saltou sobre o cão."

# Procurando por uma palavra
match = re.search("gato", text)
print(match.group())  # Saída: gato