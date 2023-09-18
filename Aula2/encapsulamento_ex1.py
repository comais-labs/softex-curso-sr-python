"""
Exemplo básico de encapsulamento em Python
O encapsulamento é uma forma de proteger os atributos de uma classe,
impedindo que sejam acessados diretamente, e ao mesmo tempo, permitindo
que sejam acessados por meio de métodos getters e setters.
"""

class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome # Atributo privado
        self.__idade = idade # Atributo privado

    def get_nome(self):
        return self.__nome
    
    def get_idade(self):
        return self.__idade
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def set_idade(self, idade):
        self.__idade = idade
    
p1 = Pessoa("João", 20)
print(f"Nome: {p1.get_nome()} Idade: {p1.get_idade()}")

# Alterando os valores dos atributos privados
p1.set_nome("Pedro")
p1.set_idade(21)
print(f"Nome: {p1.get_nome()} Idade: {p1.get_idade()}")


