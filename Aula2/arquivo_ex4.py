"""
Lendo linhas de um arquivo
"""

with open('meu_arquivo.txt', 'r') as file:  
    for line in file:  # Para cada linha no arquivo
        print(line)  # Imprime a linha
