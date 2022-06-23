s = 'America'
for i in s:
    print(i)
    print(s.index(i))

def solution(s):
    c = s[0]
    if c.isupper():    # please fix condition
        return "upper"
    elif c.isupper():  # please fix condition
        return "lower"
    elif c.isdigit():  # please fix condition
        return "digit"
    else:
        return "other"

solution(s)

position = i
print(position)
for j in s:
    if s.index(j) == position:
        print(j)


lista1 = [46360,46333,46348,46358,46265,46315,46344,46323,46322,46356,46309,46270,46302,46318,46353,46279,46364,
          46246,46281,46327,46256,46258,46259,46362,46253]

lista2 = [46246,46253,46256,46258,46259,46265,46270,46279,46281,46302,46309,46315,46318,46322,46323,46327,46333,
          46344,46348,46353,46356,46358,46360,46362,46364]

print(set(lista1) == set(lista2))

'''def print_full_name(first, last):
    print(first_name)
    print(last_name)# Write your code here
    print("Hello {} {}! You just delved into python.".format(first, last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)'''

hungry = False

if hungry:
    print("Feed me")
else:
    print("I'm full")

if True:
    print('Its True')

if 3 > 2:
    print("True")

loc = 'Bank'

if loc == 'Auto Shop':
    print("Cars are cool")
elif loc == 'Bank':
    print("Money is cool")
elif loc == 'Store':
    print("Welcome to the store")
else:
    print("I do not know much.")

name = 'Samy'

if name == 'Frankie':
    print('Hello Frankie')
elif name == 'Samy':
    print("Hello Sammy")
else:
    print("What is your name")

for num in range(1,11):
    print(num)

for num in range(1,11):
    if num % 2 == 0:
        print(f'{num} is a even number')
    else:
        print(f'{num} is a odd number')

list_sum = 0

for i in range(1, 11):
    list_sum += i
print(list_sum)

for letter in 'Hello World':
    print(letter)

# Cuando no importa el nombre de la variable
for _ in "Hello World":
    print("Cool")

tup = (1,2,3)

for item in tup:
    print(item)

# Tupple unpacking
mylist = [(1,2),(3,4),(5,6),(7,8)]

for a,b in mylist:
    print(a)
    print(b)

mylist = [(1,2,3), (5,6,7), (8,9,10)]
for a,b,c in mylist:
    print(b)

# Dictionary
d = {'k1':1, 'k2':2, 'k3':3}
for key, value in d.items():
    print(value)

# Print dictionary values
for values in d.values():
    print(values)

# While loops
print("While LOOPS")
x1 = 0
x2 = 50
while x2 < 5:
    print('this is x:',  x2)
    x2 += 1
else:
    print("X is not less than five")


print("BREAK, CONTINUE, PASS")
# Pass: Does nothing at all
for _ in range(1, 4):
    pass

print('end of my script')

# Continue: Goes to the top of the closest enclosing loop
mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

# Break: Breaks out of the current closest enclosing loop
for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 0

while x <5:
    if x == 2:
        break
    print(x)
    x += 1

print("------SPECIAL FUNCTIONS-----")

index_letter = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_letter, letter))
    index_letter += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

# Hay una manera más rápida de resolver esto con enumerate
for index, letter in enumerate(word):
    print('this is the index', index)
    print('this is the letter', letter)

# ZIP function
mylist2 = ['a', 'b', 'c']
mylist3 = [100, 200, 300]
# Siempre va realizar el match fijándose en la lista de menor cantidad de elementos
for item in zip(range(4), mylist2, mylist3):
    print(item)

#  IN operator

print("x" in [1, 2, 3])

print("x" in ['x', 'y', 'z'])

print("a" in 'a world')

d = {'mykey': 345}

print('mykey' in d)

print(345 in d.values())

# Min Function
mylist = [10, 20, 30, 40, 100]

print(min(mylist))

# MAx Function
print(max(mylist))

# Shuffle function
from random import shuffle

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
shuffle(mylist)
print(mylist)

# PAra un número aleatorio
from random import randint

print(randint(0, 100))

'''# Input function
result = int(input('Enter a number here: '))
print(result)'''



