import re

# podemos escribir expresiones regulares
# Por ejemplo para
Phone = "(555)-555-5555"

# un ejemplo puede ser
r'(\d\d\d)-\d\d\d-\d\d\d\d'
# Otro con multiplicadores
r'(\d{3})-\d{3}-\d{4}'

text = "The agent's phone number is 408-555-1234. Call soon"
print('phone' in text)

# Para usar la librería re

# Cuando no está en el texto retorna NONE
pattern = 'NOT In TEXT'
a = re.search(pattern, text)
print(a)

# Cuando está en el texto retorna la posición dentro del él , como span
pattern = 'phone'
a = re.search(pattern, text)
print(a)
#Podemos extraer diferente información del match
print(a.span())
# Indice donde comienza
print(a.start())
# Donde termina
print(a.end())
# Con esta función sólo podremos encontrar la 1era coincidencia
# Para encontrar todas las coincidencias usamos .findall
text = 'my phone once, my phone twice'

match = re.search('phone', text)
print('1', match)

matches = re.findall('phone', text)
print('2', matches)
# PAra saber cuantos coincidencias existían sacamos longitud de las listas
print(len(matches))

# para iterar sobre el objeto y obtener la ubicación de las múltiples coincidencias usamos finditer
for match in re.finditer('phone', text):
    print(match.start())

text = 'My phone number is 408-555-1234'

phone = re.search(r'\d{3}-\d{3}-\d{4}', text)
print(phone)

# Si queremos juntar dos expresiones regulares podemos hacer compile y separa los grupos por paréntesis
phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
results = re.search(phone_pattern, text)
print(results.group())

# Se comienzan a enumerar los índices en uno para este caso puntual
print(results.group(1))


# Additional Regex Syntax
# Or opperator |
# cat or dog (cat|dog)
result = re.search(r'cat|dog', 'The dog is here')
print(result)
# wild card operator (.), for instance I want the first letter in the word with at
# wild card also counts white spaces
result = re.findall(r'...at', 'The cat in the hat went splat')
print(result)
# I want find everything starts with a number
result = re.findall(r'^\d', '1 is a number')
print(result)

# I want find everything ends with a number
result = re.findall(r'\d$', 'The number is 2')
print(result)

# para excluir caracteres usamos el [] para colocarlos como una lista
phrase = 'there are 3 numbers 34 inside 5 this sentence'
# quiero excluir los numeros
pattern = r'[^\d]+'
result = re.findall(pattern, phrase)
print(result)

# se usa comúnmente para extraer puntuación de una oración
test_phrase = 'This is a string! But it has puntuaction. How can we remove it?'
result = re.findall(r'[^!.? ]+', test_phrase)
print(' '.join(result))

# Now we want inclusion
text = 'Only find the hyphen-words in this sentence. But you do not know how long-ish they are'
# [] para que me la lista, w para caracteres alfanuméricos, + para que halle tantas ocurrencias como existan
pattern = r'[\w]+'
result = re.findall(pattern, text)
print(result)

# si por ejemplos queremos obtener todas las palabras con el guión
pattern = r'[\w]+-[\w]+'
result = re.findall(pattern, text)
print(result)


# For multiple options
text = 'Hello, would you like some catfish?'
texttwo = 'Hello, would you like to take a catnap?'
textthree = 'Hello , have you seen this caterpillar?'

result = re.findall(r'cat(fish|nap|claw)', text)
print(result)