"""
Exemplo do uso do while com continue
"""
while True: # Temos um laço infinito, pois a condição é sempre verdadeira
    number = int(input("Digite um número inteiro positivo: "))
    if number < 0:
        print("Aceitamos apenas números positivos.")
        continue
    fat = 1
    while number > 0:
        fat *= number
        number -= 1
    print("Fatorial: ", fat)