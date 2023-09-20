# Definindo o cardápio com comidas e preços
cardapio = {
    "Pirarucu às natas": 20.00,
    "Moqueca tocantinense": 15.00,
    "Chambari cabuloso": 30.00,
    "Pastel sol dourado": 10.00,
    "Chambasol": 18.00,
    "Calzone la deguste": 18.00,
}

# Definindo um dicionário para armazenar os votos
votos = {item: 0 for item in cardapio}


# Função para exibir o cardápio
def exibir_cardapio():
  print("\nCardápio:")
  cont = 0
  for item, preco in cardapio.items():
    print(f"{cont} - {item}: R$ {preco:.2f}")
    cont += 1
  return cont


# Função para receber um voto
def votar():
  num_itens = exibir_cardapio()
  indice_comida = int(
      input(
          f"\nDigite qual da comida (0 a {num_itens-1}) que você gostaria de votar: "
      ))
  comidas_disponiveis = cardapio.keys()
  if indice_comida in range(num_itens):
    comida_key = list(comidas_disponiveis)[indice_comida]
    votos[comida_key] += 1
    print(f"Você votou em {comida_key}!")
  else:
    print("Comida não encontrada no cardápio.")


# Função para exibir os resultados da votação
def exibir_resultados():
  print("\nResultados da Votação:")
  for comida, total_votos in votos.items():
    print(f"{comida}: {total_votos} votos")


# Função principal
def main():
  print("Bem-vindo ao Festival Gastronômico de Taquaruçu!")
  while True:
    print("\nEscolha uma opção:")
    print("1. Ver Cardápio")
    print("2. Votar em uma Comida")
    print("3. Exibir Resultados")
    print("4. Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
      exibir_cardapio()
    elif opcao == "2":
      votar()
    elif opcao == "3":
      exibir_resultados()
    elif opcao == "4":
      print("Encerrando o Festival Gastronômico. Até a próxima!")
      break
    else:
      print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
  main()
