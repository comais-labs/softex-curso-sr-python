# Exemplo básico de pacotes úteis NumPy

import numpy as np

# Criando um array NumPy
a = np.array([1, 2, 3])
print(a)

# Criando um array NumPy com elementos do tipo float
b = np.array([1.0, 2.0, 3.0])
print(b)

# Criando um array NumPy com elementos do tipo float
c = np.array([1, 2, 3], dtype=float)
print(c)

# Criando um array NumPy com elementos do tipo string
d = np.array(["Python", "Java", "C"])
print(d)

# Criando um array NumPy com elementos do tipo string
e = np.array(["Python", "Java", "C"], dtype=str)
print(e)

# Criando um array NumPy com elementos do tipo string
f = np.array(["Python", "Java", "C"], dtype="S")
print(f)

# Criando um array NumPy com elementos do tipo string
g = np.array(["Python", "Java", "C"], dtype="U")
print(g)

# Criando um array NumPy com elementos do tipo string
h = np.array(["Python", "Java", "C"], dtype="O")
print(h)

# Criando um array NumPy com elementos do tipo string
i = np.array(["Python", "Java", "C"], dtype=object)
print(i)

# Criando um array NumPy com elementos do tipo string
j = np.array(["Python", "Java", "C"], dtype=np.unicode_)
print(j)
