def func():
    return 1


def hello():
    print("Hello!")
    return "Hello!"


# Puedo asignar una función a una variable
# Las funciones son objectos que pueden ser pasadas dentro de otro objecto
greet = hello

greet()

def hello(name='Moises'):
    print('The hello() function has been executed!')

    def greet():
        return "\t This is the greet() function inside hello"

    def welcome():
        return '\t This is welcome() inside hello'

    print("I am going to return a function!")

    if name == 'Moises':
        return greet()
    else:
        return welcome()


# Para acceder a la función greet() fuera de la función hello, tengo que llamar a la función hello
my_new_func = hello('Moses')

print(my_new_func)


def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool


some_func = cool()

print(some_func())


def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

other(hello)


# CREATE a new decorator

def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before original function')

        original_func()

        print('Some extra code, after the original function!')
    return wrap_func


def func_needs_decorator():
    print('I want to be decorated!')


# Para incluir la nueva función que necesita ser decorada en la función que ya habíamos construido
# la ponemos como parámetro de la función, pero solo la llamamos, no la ejecutamos
decorated_func = new_decorator(func_needs_decorator)

decorated_func()

# Hay una manera más fácil de hacer esto y es agregándole un @ que funciona como el decorator
@new_decorator
def func_needs_decorator():
    print('I want to be decorated!')

func_needs_decorator()