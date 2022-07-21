import math
import random

value = 4.35
value1 = 5.35
print(math.floor(value))
print(math.ceil(value))
print(round(value))
print(round(value1))

print(random.randint(0,100))
# Seed
#random.seed(101)

print(random.randint(0,100))

# Para tomar un elemento aleatorio de una lista
mylist = [x for x in range(20)]
a = random.choice(mylist)
print(a)

# Para tomar múltiples elementos aleatorios de una lista
#Sample with replacement - Permite que el mismo elemento sea elegido múltiples veces
mylist2 = random.choices(population = mylist, k = 10)
print(mylist2)
# Sample without replacement - No permite que el numero sea elegido dos veces
mylist3 = random.sample(population=mylist, k = 10)
print(mylist3)

# Shuffle list
random.shuffle(mylist3)

