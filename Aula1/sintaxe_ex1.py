# Este é um comentário em Python. Começa com o símbolo '#'

# Aqui está como você define variáveis
a = 10  # uma variável do tipo inteiro
b = "Hello, World!"  # uma variável do tipo string
c = 3.14  # uma variável do tipo float

# Impressão de valores
print(a)
print(b)
print(c)

# Operações matemáticas básicas
d = a + 5  # Adição
print(d)

e = a - 5  # Subtração
print(e)

f = a * 2  # Multiplicação
print(f)

g = a / 2  # Divisão
print(g)

h = a ** 2  # Exponenciação
print(h)

i = a % 3  # Módulo
print(i)

# Operações com strings
print(b + " " + b)  # Concatenação

# Operações com floats
print(c + 2.86)


# Listas
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Acessando elementos da lista
print(my_list[0])  # imprimir o primeiro elemento
print(my_list[-1])  # imprimir o último elemento

# Loops
for i in my_list:
    print(i)

# Condicionais
if a > 5:
    print("a é maior que 5")
else:
    print("a é menor ou igual a 5")

# Funções
def minha_funcao(x):
    return x * x

print(minha_funcao(5))  # imprimir o quadrado de 5
