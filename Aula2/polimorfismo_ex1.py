# Exemplo básico de polimorfismo em Python

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError("A classe filha precisa implementar este método")

    def comer(self):
        print(f"{self.__nome} está comendo...")

class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala uau uau!")

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala miau!")

class Rato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f"{self._Animal__nome} fala algo...")

# Testando as classes
felix = Gato("Felix")
felix.comer()
felix.falar()

pluto = Cachorro("Pluto")
pluto.comer()
pluto.falar()

mickey = Rato("Mickey")
mickey.comer()
mickey.falar()

# Testando o polimorfismo
print("\nTestando o polimorfismo...")
for animal in [felix, pluto, mickey]:
    animal.falar()

# Testando o polimorfismo com função
def teste_polimorfismo(animal):
    animal.falar()

print("\nTestando o polimorfismo com função...")
teste_polimorfismo(felix)
teste_polimorfismo(pluto)
teste_polimorfismo(mickey)

# Testando o polimorfismo com função e loop
print("\nTestando o polimorfismo com função e loop...")
animais = [felix, pluto, mickey]
for animal in animais:
    teste_polimorfismo(animal)

# Testando o polimorfismo com função e loop
print("\nTestando o polimorfismo com função e loop...")
animais = [felix, pluto, mickey]
for animal in animais:
    animal.comer()
    animal.falar()

# Testando o polimorfismo com função e loop
print("\nTestando o polimorfismo com função e loop...")
animais = [felix, pluto, mickey]
for animal in animais:
    if isinstance(animal, Gato):
        animal.falar()
    elif isinstance(animal, Cachorro):
        animal.falar()
    elif isinstance(animal, Rato):
        animal.falar()
    else:
        print("O animal não sabe falar!")
