import re  # Importa o módulo de expressões regulares

# Definindo uma string
text = "O gato saltou sobre o cão."

# Encontrando todas as ocorrências de um padrão
# O padrão a seguir procura por todas as palavras que começam com uma letra 'o'
pattern = "o\w*"
matches = re.findall(pattern, text)
print(matches)  # Saída: ['o', 'o', 'o', 'obre', 'o']
