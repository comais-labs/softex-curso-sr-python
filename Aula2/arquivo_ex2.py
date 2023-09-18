"""
Abrindo e lendo um arquivo
"""

file = open('meu_arquivo.txt', 'r')  # Abre o arquivo em modo de leitura ('r')
content = file.read()  # Lê todo o conteúdo do arquivo
file.close()  # Fecha o arquivo
print(content)  # Imprime o conteúdo do arquivo