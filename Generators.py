# Generator functions allow us to write a function that can send back
# a value and then later resume to pick up where it left over

def creates_cubes(n):
    result = [x**3 for x in range(n)]

    print(result)


creates_cubes(10)

#  De la manera anterior tenemos que generar toda la lista y mantenerla en memoria para ir llamando
# miembro a miembro si queremos iterar sobre ella y eso ocupa espacio en memoria
# Sino queremos generar toda la lista sino fijarnos en el último valor generado, usamos la palabra reservada yield

def creates_cubes(n):
    for x in range(n):
        yield x**3

for x in creates_cubes(10):
    print(x)

# Vamos a crear la secuencia de Fibonacci
def gen_fibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


fibra = [x for x in gen_fibon(10)]
print(fibra)


# Next function and inner function
def simple_gen():
    for x in range(3):
        yield x

for numb in simple_gen():
    print(numb)

g = simple_gen()
print(g)
print(next(g))
print(next(g))

# Iterate
s = 'hello'

for index, letter in enumerate(s):
    print(index, letter)
# Para convertir un string en un elemento iterable hay que  colocarlo como argumento en la función iter
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))





