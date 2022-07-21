from collections import Counter

mylist = [1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3]

# Supongamos que queremos contar cuantos hay de cada numero

print(Counter(mylist))

mylist = ['a', 'a', 10, 10, 10]
print(Counter(mylist))

for items in mylist:
    print(Counter(mylist).values())

# También podría contar elementos en un string
print(Counter('aaaaabbbbshshssjs'))

# Contar las palabras en una oración
sentence = "How many times does each word show up in this sentence wit a word"
print(Counter(sentence.lower().split()))

letter = 'aaaabbbbbccccccccddddddddd'
c = Counter(letter)
print(c)
print(c.most_common())
# Le puedo especificar cuantos elementos más comunes quiero, por ejemplo los 2 más comunes
print(c.most_common(2))

# También puedo obtener sólo las claves de la especie de diccionario del Counter
print(list(c))

# Default dictionary
from collections import defaultdict
d = defaultdict(lambda: 0)
d['correct'] = 100
print(d['WRONG KEY!'])


# Named tuple
from collections import namedtuple
Dog = namedtuple('Dog', ['age', 'breed', 'name'])
samy = Dog(age= 5, breed = 'Husky', name= 'Sam')
print(type(samy))
print(samy.age)
# Or you can call it by index
print(samy[0])

print(samy.breed)
print(samy.name)
