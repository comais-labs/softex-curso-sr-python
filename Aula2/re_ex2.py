import re  # Importa o módulo de expressões regulares

# Definindo uma string
text = "O gato saltou sobre o cão."

# Substituindo uma palavra
text = re.sub("cão", "muro", text)
print(text)  # Saída: O gato saltou sobre o muro.
