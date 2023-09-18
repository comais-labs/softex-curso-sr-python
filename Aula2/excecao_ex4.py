"""
O bloco finally em um bloco try/except é usado para colocar 
qualquer código que deve ser executado, independentemente 
de uma exceção ter sido lançada ou não. 
"""

try:
    # Tentamos abrir um arquivo e ler seu conteúdo
    file = open("arquivo.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    # Este bloco será executado se o arquivo não for encontrado
    print("O arquivo não foi encontrado.")
finally:
    # Este bloco será executado independentemente de uma exceção ter sido lançada ou não
    print("Finalizando a operação de leitura do arquivo.")
    if 'file' in locals():  # Verificamos se a variável 'file' foi definida
        file.close()  # Fechamos o arquivo se ele estiver aberto
