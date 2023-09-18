# Exemplo de tratamento de exceção
try:
    # código que pode lançar uma exceção
    x = 5 / 0
except ZeroDivisionError:
    # código para tratar a exceção
    print("Você tentou dividir por zero!")
