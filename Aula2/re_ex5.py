import re  # Importa o módulo de expressões regulares

# Definindo uma string
text = "O gato saltou sobre o cão."

# Dividindo uma string baseada em um padrão
# O padrão a seguir divide a string em cada espaço em branco
pattern = "\s"
parts = re.split(pattern, text)
print(parts)  # Saída: ['O', 'gato', 'saltou', 'sobre', 'o', 'muro.']
