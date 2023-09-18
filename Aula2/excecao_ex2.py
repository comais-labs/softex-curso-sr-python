# Exemplo de tratamento de execeção para mais de um tipo de exceção
try:
    # Tentamos converter uma string que não representa um número inteiro
    number = int("not_a_number")
except ValueError:
    # Este bloco será executado para ValueError
    print("A string não pode ser convertida em um número inteiro.")
except Exception as e:
    # Este bloco será executado para todas as outras exceções
    print("Ocorreu um erro: " + str(e))

