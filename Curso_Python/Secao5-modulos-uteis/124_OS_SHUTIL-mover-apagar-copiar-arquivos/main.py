import os
import shutil

original_way = r'C:\Users\pedro\Documents\series2\aaa'
new_way = r'C:\Users\pedro\Documents\series2\testando'

try:
    os.mkdir(new_way)
except FileExistsError as e:
    print(f'Pasta {new_way} já existe.')

for root, dirs, files in os.walk(original_way):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(new_way, file)
        print(old_file_path)
        if '.txt' in file:
            # shutil.move(old_file_path, new_file_path) # usa pra mover
            shutil.copy(old_file_path, new_file_path)
            # shutil.remove(new_file_path) apaga arquivos
            print(f'Arquivo {file} copiado com sucesso.')
