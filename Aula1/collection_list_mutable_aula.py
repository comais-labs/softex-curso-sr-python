#%% Append
s = [1,2,3,4]
s.append(5)
print(s)

# extend
s.extend([6, 7])
print(s)

# qualquer iterable
# note que 8 e 9 serao 
# adicionados como strings
s.extend("89")
print(s)

# insert
s = [1, 2, 4]
s.insert(2, 3)
print(s)
# se o indice for muito menor, insere antes
# se for maior, insere no final

s.insert(-50, 0)
s.insert(50, 5)
print(s)

#pop
removido = s.pop()
print(s)

removido = s.pop(-1)
print(s)

# Tentar pop com índices fora dos limites
# Gera erro
# Isto gerará erro
#s.pop(500)

# Remove
s = ["ho", "ho", "ho","ho"]
s.remove("ho")
print(s)
# Tentar remover um elemento inexistente provoca erro
# Isto gerará erro
s.remove("ieie")

#Reverse
s = list(range(5))
print(s)

s.reverse() 
print(s)

# Nao cria uma instancia nova como [::-1]
s = list(range(5))
reversed_s = s[::-1]
s is reversed_s

# %% Ordenação
s = [ 5, 7, 1, 2, 10]
s.sort()
print(s)

# problema com não comparáveis
# o codigo a seguir gerará erro
s = [ 5, "7", 1, 2, 10]
s.sort()

s.sort(key=int) 
print(s)
    
#segundo exemplo
s = ["Sandra", "Cassandra", "Ribeiro"]
# ordenar por tamanho da string
s.sort(key=len)
print(s)


#Uso de reverse
s = [ 5, 7, 1, 2, 10]
s.sort(reverse=True)
print(s)

#%% List comprehensions
# Imagine que eu queira o quadrado 
# de uma lista
s = [ 5, 7, 1, 2, 10]
quadrado_s = []
for num in s:
    quadrado_s.append(num**2)

print(quadrado_s)

# isso pode ser transformado em uma linha:
quad_comp = [num**2 for num in s]
print(quad_comp)


# Exemplo com if
# quadrados de num <= 5
quad_comp = [num**2 for num in s if num<=5]
print(quad_comp)


# Outro exemplo
v1 = [1, 7, -5]
v2 = [-9, 3, 12]
[v1[i] + v2[i] for i in range(3)]


# Outro exemplo:
letters = list("ABC")
numbers = list("123")

[(a,b) for a in letters for b in numbers]

# %%
