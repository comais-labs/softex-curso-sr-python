"""
Usando o comando 'with' para lidar automaticamente com o 
fechamento do arquivo
"""

with open('meu_arquivo.txt', 'r') as file:  
    print(file.read())  # Imprime o conteúdo do arquivo
