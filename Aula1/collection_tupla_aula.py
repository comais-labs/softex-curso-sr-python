"""
Exemplos usados em aula para tupla
"""
#%% Exemplos de tuplas 
relogio= 12,37
hora, min = relogio
print(hora)
print(min)

# %% Packing e Unpacking
s = [ 5, 7, 1, 2, 10]
cinco, *demais, dez = s
print(cinco)
print(dez)
print(demais)

*demais, dois, dez = s
print(demais)
print(dois)
print(dez)

# %% Imutabilidade de instâncias
lista = [1]
my_tuple = (lista,)
print(my_tuple)
lista.append(2)
print(my_tuple)
