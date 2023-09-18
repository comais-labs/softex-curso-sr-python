"""Este arquivo contém os exemplos da aula.
"""

# %% 1. checagem de item na lista
lista = ["um", 2, 3.0, "quatro", 5, "seis", "sete"]

"6" in lista

"seis" in lista

# %% 2.a Concatenação de listas
l1 = [1, 2]
l2 = [3, 4]
ref_l1 = l1
l1 += l2 # l1 = l1 + l2
print(l1)
print(ref_l1)

# %% 2.b Concatenação de strings
str_1 = "Joao"
str_2 = " da Silva"
ref_str_1 = str_1
str_1 += str_2
print(str_1)
print(ref_str_1)

# %% 3.a Repetição
lista = [1, 2]
lista = 3*lista
lista
lista *= 2
lista

# %% 3.b Repetição: nao faz copia
list_names = ["Joao"]
list_idades = [21]
lista = [list_names, list_idades]
lista = lista*3
lista
list_idades.append(31)
lista

# %% 4.a indexação
lista = [1, 2, 3, 4, 5]
lista[2]
lista[10] #vai produzir um erro
# %% 4.b Slicing
msg = "Palmas"
msg[1:5]
msg[-5:-1]
#pode combinar também
msg[1:-1]
# até o fim e e do início até outro
msg[:3]

msg[2:]

# %% 4.c Slicing para cópia
# Mutable
lista = [1, 2, 3, 4, 5]
lista2 = lista[:]
lista2 is lista

# Imutable
msg = "Palmas"
msg_copy = msg[:]
msg is msg_copy

# %% 4.d Slicing com passos s[i:j:k]
numeros = "0123456789"
numeros[1::2]

# Exemplo com passo negativo
numeros[4:0:-1] #perceba que a regra continua i contido até j nao contido no index
# Exemplo que não gera IndexError
numeros[1:50]


# Índices muito grandes são internamente trocados pelo máximo;

# Muito pequenos trocados pelo mínimo; 
numeros[-50:50]
# Se ambos estão fora do range válido ou se o i>j e o passo é positivo: sequência vazia;
numeros[50:100]
numeros[-50:-10]

# %% Buscando um elemento com s.index
s = [1,2,3,4,5,6,7,8,9,10,3,4,5]
s.index(10)
#gerar um erro
s.index(0)
#procurando o indice do valor 4 a partir 
# do sexto elemento
s.index(4, 5)
#procurando 3 a partir do sexto elemento 
# até o nono. Veja que o 3 está na 
# posiçao 10, mas como k<10, ele nao encontra
s.index(3, 5, 10)
#Procurando 3 a partir do sexto elemento até o de índice 10
#Veja que o 3 está na posiçao 10, 
s.index(3, 5, 11)

# %% Calculando a frequência dos elementos, min, max e tamanho
s = [3,2,2,8,9,10,3,4,5]
s.count(2)
len(s)
min(s)
max(s)
# os itens da lista devem ser comparáveis entre si,
# Senão gera em erro³
s = [3, 2.1, "quatro"]
max(s) # vai gerar erro pela incompatibilidade de comparação entre str e int
# %%
