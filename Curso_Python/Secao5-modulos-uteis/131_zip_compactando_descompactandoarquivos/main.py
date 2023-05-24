from zipfile import ZipFile
import os


path = r'\Pedro\ZipPython'
with ZipFile('file.zip', 'w') as zip:
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        zip.write(full_path, file)

with ZipFile('file.zip', 'r') as zip:
    for file in zip.namelist():
        print(file)

with ZipFile('file.zip', 'r') as zip:
    zip.extractall('descompactado')
