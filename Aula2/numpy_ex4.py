# Exemplo básico de pacotes úteis NumPy
# Indexação de Arrays

import numpy as np

a = np.array([1, 2, 3])
print(a[0])      # acessa o primeiro elemento
b = np.array([[1,2,3],[4,5,6]])
print(b[1,2])    # acessa o terceiro elemento da segunda linha
print(b[1][2])   # acessa o terceiro elemento da segunda linha
print(b[1,:])    # acessa a segunda linha inteira
print(b[:,1])    # acessa a segunda coluna inteira
print(b[0:2,1])  # acessa a segunda coluna das duas primeiras linhas
print(b[-1])     # acessa a última linha
print(b[-1,1:])  # acessa a segunda e terceira colunas da última linha
