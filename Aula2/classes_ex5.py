"""
Exemplo de classe simples demonstrando os métodos especiais,
também conhecidos como métodos dunder (double underscore).
Em Python são métodos com dois sublinhados antes e depois 
do nome. Eles são métodos especiais definidos na classe
que você pode usar para adicionar funcionalidades "mágicas"
a suas classes.

Alguns exemplos comuns de métodos especiais incluem 
__init__, __str__, __len__, e __del__.
"""

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # Método especial para representação em string do objeto
    def __str__(self):
        return f"'{self.title}' por {self.author}"

    # Método especial para obter o tamanho (neste caso, número de páginas) do objeto
    def __len__(self):
        return self.pages

    # Método especial que é chamado quando o objeto é deletado
    def __del__(self):
        print(f"'{self.title}' foi deletado.")


book1 = Book("1984", "George Orwell", 328)

# Usando __str__
print(book1)  # Saída: '1984' por George Orwell

# Usando __len__
print(len(book1))  # Saída: 328

# Usando __del__
del book1  # Saída: '1984' foi deletado.

# Sugestão de teste:
# - Comente o método __del__ e veja o que acontece.
# - Adicione outros métodos especiais à classe e teste-os.