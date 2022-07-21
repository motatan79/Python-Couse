import time
import timeit

def func_one(n):
    return [str(x) for x in range(n)]

func_one(10)


def func_two(n):
    return list(map(str, range(n)))


# PAra determinar cual es más eficiente
# Current time before run the code
start_time = time.time()
# Run code
result = func_one(1)
#Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time
print('func_one: ', elapsed_time)


# Current time before run the code
start_time = time.time()
# Run code
result = func_two(1)
#Current time after running code
end_time = time.time()
# Elapsed time
elapsed_time = end_time - start_time
print('func_two: ', elapsed_time)


# Muchas veces cuando los códigos se ejecutan muy rápido resulta imposible medir el tiempo
# por ello se usa la librería timeit
# para ello necesitamos tres parámetros
# 1) la evaluación del código como un string
stmt = '''
func_one(100)
'''
# 2) el código a ejecutar como un string
setup = '''
def func_one(n):
    return [str(x) for x in range(n)]'''
# 3) la cantidad de veces que se va ejecutar el código como numero

a = timeit.timeit(stmt, setup, number=10000)
print('func_one: ', a)

# PAra comparar la ejecución con la función 2
stmt = '''
func_two(100)
'''
setup = '''
def func_two(n):
    return list(map(str, range(n)))
'''
a = timeit.timeit(stmt, setup, number=10000)
print('func_two: ', a)