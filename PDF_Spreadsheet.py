import csv
import PyPDF2

# Open the file
data = open('example.csv', encoding='utf-8')
# csv.reader
csv_data = csv.reader(data)
# reformat it into a python object list of list
data_lines = list(csv_data)

# Columns names
data_lines[0]


for line in data_lines[:5]:
    print(line)

all_emails = [line[3] for line in data_lines[1:]]
print(all_emails)

full_names = [line[1] + ' ' + line[2] for line in data_lines[1:]]
print(full_names)

# Para escribir el .csv
file_to_output = open('to_save_file.csv', mode='w', newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
file_to_output.close()

# Working with PDF Files
# 1er Paso Leer el archivo con open and rb mode
f = open('Working_Business_Proposal.pdf', 'rb')

# Convertir el archivo a un objeto legible
pdf_reader = PyPDF2.PdfFileReader(f)

# para saber el numero de páginas
print(pdf_reader.numPages)

# para obtener la primera página
page_one = pdf_reader.getPage(0)

# PAra ver el texto en esa página y ver si funciona para extraer el texto
# Si el resultado es un string vacío eso implica que nuestro PDF no se puede convertir con esta librería
page_one_text = page_one.extractText()
print(page_one_text)

# PAra cerrarlo
f.close()

# Add pages to a PDF
f = open('Working_Business_Proposal.pdf', mode='rb')

pdf_reader = PyPDF2.PdfFileReader(f)

# Para trabajar en la primera página
first_page = pdf_reader.getPage(0)

# Queremos traer todas las primeras páginas de diferentes archivos PDF's
pdf_writer = PyPDF2.PdfFileWriter()

# la página a insertar ya debe estar convertida a PyPDF2.pdf.PageObject
pdf_writer.addPage(first_page)

pdf_output = open('Some_BrandNew_Doc.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()

# Working with a loop to grab all text in a text file
f = open('Working_Business_Proposal.pdf', 'rb')

pdf_text = []

pdf_reader = PyPDF2.PdfFileReader(f)

for num in range(pdf_reader.numPages):
    page = pdf_reader.getPage(num)
    pdf_text.append(page.extractText())

print('This is a new text')
print(pdf_text[1])