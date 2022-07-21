import os
import shutil
import send2trash

'''f = open('practice.txt', 'w+')
f.write('This is a test string')
f.close()'''

# Para obtener el cwd (current working directory)
print(os.getcwd())

# PAra obtener todo lo que esté en un directorio
print(os.listdir())

# para mover archivos entre diferentes carpetas
#shutil.move('C:\\Users\\m.pirela.escobar\\OneDrive - Accenture\\Documents\\Courses\\practice.txt', os.getcwd())

# para borrar archivos con send2trash
#send2trash.send2trash('practice.txt')

# PAra obtener todo lo que esté en un directorio
print(os.listdir())

# Para tener una lista de archivos y directorios
for folder, sub_folders, files in os.walk(os.getcwd()):

    print(f'Currently looking at {folder}')
    print('\n')
    print('The subfolders are: ')
    for sub_fold in sub_folders:
        print(f'\t Subfolder: {sub_fold}')

    print('\n')
    print("the files are: ")
    for f in files:
        print(f'\t File: {f}')
    print('\n')