"""
Exemplo de classe simples demonstrando o polimorfismo, que 
permite que subclasses de uma classe usem métodos da 
classe pai como se fossem seus próprios, mas com 
comportamento possivelmente diferente.
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

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    """
    Sobrescrevendo o método greet da classe Person.
    """
    def greet(self):
        print(f"Olá! Meu nome é {self.name}, eu tenho {self.age} anos e estou estudando {self.course}.")

# Criando instâncias das classes Person e Student
person1 = Person("Alice", 25)
student1 = Student("Bob", 20, "Python")

# Chamando o método greet em ambos os objetos
person1.greet()  # Saída: Olá! Meu nome é Alice e eu tenho 25 anos.
student1.greet()  # Saída: Olá! Meu nome é Bob, eu tenho 20 anos e estou estudando Python.

# Sugestão de teste:
# Comente o método greet da classe Student e veja o que acontece.