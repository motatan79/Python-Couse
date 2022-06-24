mystring = 'hello'

mylist = []
mylist2 = []
for a, b in enumerate(mystring):
    mylist.append(b)
print(mylist)

for letter in mystring:
    mylist2.append(letter)
print(mylist2)

# List Comprehension
mylist3 = [letter for letter in mystring]
print(mylist3)

mylist = [x**2 for x in range(0, 11)]
print(mylist)

# Para tener sólo pares
mylist = [x for x in range(11) if x % 2 == 0]
print(mylist)

celsius = [0, 10, 20, 34.5]
fahrenheit = [((9/5)*temp + 32) for temp in celsius]
print(fahrenheit)

# Nested Loop
mylist = []

for x in [2, 4, 6]:
    for y in [1, 10, 1000]:
        mylist.append(x*y)
print(mylist)

mylist = [x*y for x in [2, 4, 6] for y in [1, 10, 1000]]
print(mylist)
