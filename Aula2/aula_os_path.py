#%% Testando se um path existe

from os.path import exists
import os
print(os.getcwd())
exists("temp")
# %%
from os.path import getatime, isdir, islink, isfile
from datetime import datetime
path = "aula_os_path.py"
access_time = getatime(path)
d = datetime.fromtimestamp(access_time)
print(d)
isfile(path), isdir(path), islink(path)
# %% Parte II
from os.path import join
current_dir = os.getcwd()
print(current_dir)
temp1 = join(current_dir, "temp", "temp1")
print(temp1)
# %%
from os.path import join, split
import os
current_dir = os.getcwd()
# print(current_dir)

temp1 = join(current_dir, "temp", "arquivo1.txt")
print(temp1)
dir, filename = split(temp1)
print(dir, filename)
#%% 
# em um diretório, ele separa o último item.
temp1 = join(current_dir, "temp", "temp1")
dir, filename = split(temp1)
print(dir, filename)


# %%
import os
from os.path import join, splitext
current_dir = os.getcwd()
temp1 = join(current_dir, "temp", "arquivo1.txt")
filepath, ext = splitext(temp1)
print(filepath, ext)
#caso opath seja um diretório
temp1 = join(current_dir, "temp", "temp1")
filepath, ext = splitext(temp1)
print(filepath, ext)
# %%
