import zipfile
import shutil

f = open('fileone.txt', 'w+')
f.write('ONE FILE')
f.close()

f = open('filetwo.txt', 'w+')
f.write('TWO FILE')
f.close()

comp_file = zipfile.ZipFile('comp_file.zip', 'w')

# para comprimir los archivos
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

# Para extraer los archivos del zip
zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
# aquí decidimos donde dejar los archivos
zip_obj.extractall('extracted_content')

# para convertir la carpeta recién creada en un zip folder usando la librería shutil
dir_to_zip = "C:\\Users\\m.pirela.escobar\\OneDrive - Accenture\\Documents\\Courses\\Python\\extracted_content"
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)

# Para extraer los archivos de la carpeta
shutil.unpack_archive('example.zip', 'final.zip', 'zip')

# Para extraer los archivos de la carpeta
shutil.unpack_archive('unzip_me_for_instructions.zip', 'final.zip', 'zip')
