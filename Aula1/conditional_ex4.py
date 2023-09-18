"""
Exemplo de desvio condicional aninhado.
"""
x = 10
if x > 0:
    print("x é positivo")
    if x % 2 == 0:
        print("x é par")
    else:
        print("x é impar")
else:
    print("x é negativo ou zero")
