# Exemplo de docstring com parâmetros
def fat2(n):
    '''
    Entre com fat2(n) para calcular o fatorial de n
    Exemplo: fat2(5)
    Parâmetros:
        n: número inteiro
    Retorno:
        fatorial de n
    '''
    if (n <= 1):
       return 1
    return n * fat2(n-1)

help(fat2)