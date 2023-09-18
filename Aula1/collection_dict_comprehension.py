''' Exemplo de dict comprehension.
'''
names = ["Darla", "Silvio", "Domingos", "Gilberto"]
d = {k: len(k) for k in names}
print(d)
dict_start_with_letter_d = {k: len(k) for k in names if k[0] == "D"}
print(dict_start_with_letter_d)