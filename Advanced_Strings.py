s  ='hello World'

# Changes cases upper and lower
# Para poner la primera letra de la 1era palabra en mayúscula
print(s.capitalize())

# Todas en mayúsculas
print(s.upper())

# Todas en minúsculas
print(s.lower())

# Para contar cuantas letras de una hay en el string
print(s.count('o'))

# para encontrar el índice de la primera ocurrencia
print(s.find('o'))

# Si quieres centrar tu texto rodeado de otro caracter
print(s.center(20, 'z'))

# Expand Tabs
print('hello\thi'.expandtabs())

s = 'hello'

# Chequear si todos los caracteres son alfanuméricos
print(s.isalnum())

# Chequear si todos son alfabéticos
print(s.isalpha())

# Chequear si todos son minúsculas
print(s.islower())

# Chequear si hay espacios en blanco
print(s.isspace())

# Chequear si es tipo título
print(s.istitle())

# Chequear si todos son mayúsculas
print(s.isupper())

# Chequear si termina con
print(s.endswith('o'))
# o también podría ser
print(s[-1] == 'o')

# REGULAR EXPRESSIONS

# Para separar el string de acuerdo a una letra, genera una lista
print(s.split('e'))

# Partition, taking account only first instance. Y como resultado trae lo que está antes del
# elemento señalado para la partición, el elemento de partición y de último lo que está después del
# elemento de partición
s = 'hiihihihihihhhi'
print(s.partition('i'))






