"""
Exemplo do conceito de herança utilizando duas classes simples, 
onde uma classe Student que herda de Person.
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

"""
Classe Student herda de Person
"""
class Student(Person):
    """
    Inicializa a classe Student com os atributos name, age e course.
    """
    def __init__(self, name, age, course):
        super().__init__(name, age)  # chamando o construtor da classe pai
        self.course = course  # atributo adicional
    """
    Método que imprime uma mensagem de estudo.
    """
    def study(self):
        print(f"{self.name} está estudando {self.course}.")

# Criando uma instância da classe Student
student1 = Student("Bob", 20, "Python")

# Acessando atributos
print(student1.name)  # Saída: Bob
print(student1.age)  # Saída: 20
print(student1.course)  # Saída: Python

# Chamando o método greet herdado da classe Person
student1.greet()  # Saída: Olá! Meu nome é Bob e eu tenho 20 anos.

# Chamando o método study da classe Student
student1.study()  # Saída: Bob está estudando Python.