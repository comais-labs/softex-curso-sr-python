"""Este módulo explora algumas funções do sitema de arquivos"""
# %% 
import os
print(os.listdir())
# a constante __file__ só existe se o 
# arquivo for passado para o interpretador
# python arquivo.py
print(__file__)
print(os.path.dirname(__file__))
os.chdir(os.path.dirname(__file__))

# %%
for path in os.walk("temp"):
    print(path)
   
# %%³
# chmod 000 temp1

import os
def onError(erro):
    print("Deu erro em :", erro)

for path in os.walk("temp", True, onError):
    print(path)

#('temp', ['temp2', 'temp1'], ['arquivo1.txt'])
#('temp/temp2', ['child-folder'], ['arq_on_folder_temp2.txt'])
#('temp/temp2/child-folder', [], [])
#Deu erro em : [Errno 13] Permission denied: 'temp/temp1'
