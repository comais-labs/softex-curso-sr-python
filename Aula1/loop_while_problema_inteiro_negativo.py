""" 
Exemplo do uso do mecanismo continue em um laço while

"""

while True: # Temos um laço infinito, pois a condição é sempre verdadeira
    number = int(input("Digite um número inteiro positivo: "))
    fat = 1
    while number > 0:
        fat *= number
        number -= 1
    print("Fatorial: ", fat)
    