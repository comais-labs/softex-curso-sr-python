"""
Exemplo de jogo de adivinhação de um número feito com while 
e mecanismo de saída break e detecção de fim do laço
"""
numero_sorteado = 12
palpite = 0
print("O jogo funciona com números inteiros positivos.")
while palpite != numero_sorteado:
    palpite = int(input("Digite seu palpite ou 0 (zero) para encerrar o jogo: "))
    if palpite == 0:
        print("Encerrando o jogo.")
        break
else:
    print("Você acertou! O número era ", numero_sorteado)
    