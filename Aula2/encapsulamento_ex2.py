# Exemplo básico de encapsulamento em Python utilizando o decorator @property

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome # Atributo privado
        self.__idade = idade # Atributo privado

    @property # Getter
    def nome(self):
        print("Chamando @property nome()")
        return self.__nome
    
    @property # Getter
    def idade(self):
        return self.__idade
    
    @nome.setter # Setter
    def nome(self, nome):
        print("Chamando setter nome()")
        self.__nome = nome
    
    @idade.setter # Setter
    def idade(self, idade):
        self.__idade = idade

p1 = Pessoa("João", 20)
p1.nome = "João"
p1.idade = 20
print(f"Nome: {p1.nome} Idade: {p1.idade}")
