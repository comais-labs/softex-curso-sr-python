"""O objetivo deste módulo é ilustrar o funcionamento das exceptions"""


#%% Tratando uma exceção
def get_file(name):
    try:
        return open(name)
    except FileNotFoundError:
        return None
get_file("arquivo_inexistente")    
    
#%% Capturando mais de uma exceção    
def get_file(name):
    try:
        return open(name)
    except FileNotFoundError:
        return None
    except TypeError:
        return None

#%% Exemplo de captura de várias exceções
try:
    print([1,2,3][10])
except (IndexError, TypeError) as e:
    print("Error message:", e.args[0])
    