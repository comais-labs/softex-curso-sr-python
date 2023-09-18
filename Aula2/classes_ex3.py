"""
Exemplo de classe simples demonstrando o encapsulamento, que 
se refere à restrição do acesso a métodos e variáveis.
"""

class Person:
    def __init__(self, name, age):
        self.name = name  # public
        self.__age = age  # private

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Idade inválida")

    def get_age(self):
        return self.__age


person = Person("Alice", 30)

print(person.name)  # Saída: Alice
print(person.get_age())  # Saída: 30
# print(person.__age)  # isso causará um erro, porque __age é privado

person.set_age(-1)  # Saída: Idade inválida
person.set_age(25)
print(person.get_age())  # Saída: 25
