import re  # Importa o módulo de expressões regulares

# Definindo uma string
text = "O gato saltou sobre o cão."

# Procurando por um padrão
# O padrão a seguir procura por qualquer palavra que comece com 's' e termine com 'u'
pattern = "s\w*u"
match = re.search(pattern, text)
print(match.group())  # Saída: saltou
