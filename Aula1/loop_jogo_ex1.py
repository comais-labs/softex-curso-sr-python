"""
Exemplo de jogo de adivinhação de um número feito com while
"""
numero_sorteado = 12
palpite = 0
while palpite != numero_sorteado:
    palpite = int(input("Digite seu palpite (num inteiro positivo): "))

print("Você acertou! O número era ", numero_sorteado)