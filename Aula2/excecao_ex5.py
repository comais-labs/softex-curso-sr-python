"""
Exemplo de uso da palavra-chave raise para lançar uma
exceção em Python. Isso é útil quando você quer
sinalizar que algo inesperado aconteceu por seu código
não está preparado para lidar.
"""

def divide(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print("Ocorreu um erro:", e)
