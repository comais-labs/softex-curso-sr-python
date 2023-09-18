"""
Exemplo de classe simples, chamada Person, que terá name (nome) e
age (idade) como atributos e um método greet (cumprimentar).
"""

class Person:
    """
    Inicializa a classe Person com os atributos name e age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    """
    Método que imprime uma mensagem de cumprimento.
    """
    def greet(self):
        print(f"Olá! Meu nome é {self.name} e eu tenho {self.age} anos.")

# Criando uma instância da classe Person
person1 = Person("Alice", 25)

# Acessando atributos
print(person1.name)  # Saída: Alice
print(person1.age)  # Saída: 25

# Chamando o método greet
person1.greet()  # Saída: Olá! Meu nome é Alice e eu tenho 25 anos.
