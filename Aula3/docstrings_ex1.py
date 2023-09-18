# Docstrings: Documentação de funções

def fat1(n):
    '''
    Entre com fat1(n) para calcular o fatorial de n
    Exemplo: fat1(5)
    '''
    if (n <= 1):
       return 1
    return n * fat1(n-1)

# Como consultar a documentação de uma função via Prompt de Comando:
# Forma 1:
help(fat1)

# Forma 2:
print(fat1.__doc__)
# %%
# Como consultar a documentação de uma função via Jupyter Notebook:
# Forma 1:
?fat1

# Forma 2:
??fat1