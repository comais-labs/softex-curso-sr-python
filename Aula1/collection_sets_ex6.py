"""
Coleções em Python:
- Sets: Verificando se um item existe em um set.
"""

set1 = set(("banana", "maçã", "uva", "abacaxi", "laranja", "melancia"))
# Uma forma de verificar se um item existe em um set
print("banana" in set1)

# outra forma de verificar se um item existe em um set
if "banana" in set1:
    print("Sim, 'banana' está no set1")
