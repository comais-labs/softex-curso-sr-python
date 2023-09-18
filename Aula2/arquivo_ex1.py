"""
Escrevendo em um arquivo
"""
file = open('meu_arquivo.txt', 'w')  # Abre o arquivo em modo de escrita ('w')
file.write('Olá, mundo!')  # Escreve 'Olá, mundo!' no arquivo
file.close()  # Fecha o arquivo
