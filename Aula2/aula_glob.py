"""Neste módulo ilustramos o uso
do glob para acesso a arquivos"""

import glob
# chamar o interpretador dentro da pasta Aula2
# %% Listar todos os arquivos e pastas em um caminho

for file in glob.glob("./arquivos/*"):
    print(file)

# %% Listar todos os arquivos e pastas em um caminho de maneira recursiva

for file in glob.glob("./arquivos/**", recursive=True):
    print(file)

# %% Listar somente os arquivos com alguma extensão

for file in glob.glob("./arquivos/**/*.*", recursive=True):
    print(file)


# %% Listar somente os arquivos com uma extensão específica

for file in glob.glob("./arquivos/**/*.png", recursive=True):
    print(file)

# %% Listar somente os arquivos com uma extensão específica e com um padrão de nomes

for file in glob.glob("./arquivos/**/img*.png", recursive=True):
    print(file)

# %% Listar somente os arquivos com uma extensão específica e com um padrão de nomes 2

for file in glob.glob("./arquivos/**/img?.png", recursive=True):
    print(file)


# %% Listar arquivos de pastas que só estão em letras

for file in glob.glob("./arquivos/*[a-z]/**/*.txt", recursive=True):
    print(file)
