import re

# Texto de entrada com endereços de e-mail
texto = "Este é um exemplo de texto com vários endereços de e-mail, como exemplo1@email.com, email2@example.com.br, e inválido@example."

texto=re.sub(',', ' ', texto)

palavras=re.split('\s', texto)

for email in palavras:
    padrao_email = r'([A-Za-z0-9_]+@[A-Za-z0-9_]+\.[a-z]{2,3}(\.[a-z]{2})?)'
    if(re.fullmatch(padrao_email, email)):
        print(email)
      
'''
import re

# Texto de entrada com endereços de e-mail
texto = "Este é um exemplo de texto com vários endereços de e-mail, como exemplo1@email.com, email2@example.com.br, e inválido@example."

# Usando uma expressão regular para encontrar endereços de e-mail
padrao_email = r'([A-Za-z0-9_]+@[A-Za-z0-9_]+\.[a-z]{2,3}(\.[a-z]{2})?)'
emails_encontrados = re.findall(padrao_email, texto)

# Exibindo os endereços de e-mail encontrados
print("Endereços de E-mail Encontrados:")
for email in emails_encontrados:
    print(email[0])
'''