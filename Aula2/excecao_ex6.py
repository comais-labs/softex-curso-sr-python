""" Exemplo de exceções personalizadas em Python"""

class UnknownAnimalError(Exception):
    """Exceção lançada para erros na categoria de animais desconhecidos."""
    def __init__(self, animal, message="Animal desconhecido."):
        self.animal = animal
        self.message = message
        super().__init__(self.message)

def add_animal(inventory, animal):
    known_animals = ['cachorro', 'gato', 'papagaio']
    if animal not in known_animals:
        raise UnknownAnimalError(animal)
    else:
        inventory.append(animal)

inventory = []
try:
    add_animal(inventory, 'leão')
except UnknownAnimalError as e:
    print(f"Erro: {e.message} - '{e.animal}' não é um animal reconhecido.")
