import re

# Definindo o texto
text = "Olá, mundo! Como você está? Hoje é um bom dia."

# Definindo o padrão para os caracteres de pontuação
pattern = r"[.!?]"

# Dividindo o texto usando a expressão regular
sentences = re.split(pattern, text)

# Imprimindo as sentenças
for sentence in sentences:
    # remove espaços em branco extras do início e do final da string
    sentence = sentence.strip()  
    print(sentence)
