class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        raise NotImplementedError("Método 'atacar' não implementado para este personagem!")

class Guerreiro(Personagem):
    def atacar(self):
        return f"{self.nome} ataca com uma espada!"

class Mago(Personagem):
    def atacar(self):
        return f"{self.nome} lança uma bola de fogo!"

class Inimigo:
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida

    def atacar(self):
        raise NotImplementedError("Método 'atacar' não implementado para este inimigo!")

class Zumbi(Inimigo):
    def atacar(self):
        return f"{self.nome} morde!"

class Dragao(Inimigo):
    def atacar(self):
        return f"{self.nome} cospe fogo!"

# Função para personagens atacarem inimigos
def personagem_atacar_inimigo(personagem, inimigo):
    try:
        acao = personagem.atacar()
        print(acao)
        print(f"{inimigo.nome} sofreu um dano!")
    except NotImplementedError as e:
        print(f"Erro: {e}")
    except Exception as ex:
        print(f"Ocorreu um erro inesperado: {ex}")

# Criando instâncias de personagens e inimigos
guerreiro = Guerreiro("Aragorn", 100)
mago = Mago("Gandalf", 80)
zumbi = Zumbi("Zumbi Assustador", 50)
dragao = Dragao("Smaug", 150)

# Personagens atacam inimigos
personagem_atacar_inimigo(guerreiro, zumbi)
personagem_atacar_inimigo(mago, dragao)
personagem_atacar_inimigo(dragao, guerreiro)
personagem_atacar_inimigo(zumbi, mago)
personagem_atacar_inimigo(zumbi, Personagem("Personagem Incompleto", 70))