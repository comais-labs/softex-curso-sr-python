"""
O bloco else em um bloco try/except é executado
quando nenhuma exceção ocorre no bloco try.
É útil quando você tem um pedaço de código que
só deve ser executado se não houve exceções.
"""

try:
    # Tentamos converter uma string para um número inteiro
    number = int("123")
except ValueError:
    print("A string não pode ser convertida em um número inteiro.")
else:
    print("A conversão foi bem-sucedida.")
    print("O número é:", number)
