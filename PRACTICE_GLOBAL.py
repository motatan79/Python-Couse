stock_prices = [('APPLE', 20000), ('GOOGLE', 400), ('MSC', 4000)]

lista = [a for a, b in stock_prices]
print(lista)

def myfunc(stock_prices):
    value = 0
    for a, b in stock_prices:
        if b > value:
            value = b
    print(value)

myfunc(stock_prices)

work_hours = [('Abby', 10000), ('Billy', 4000), ('Cassie', 800)]

def employee_of_month(work_hours):
    value = 0
    name = ''
    for employee, hours in work_hours:
        if hours > value:
            value = hours
            name = employee

    print(f'the employee of the month is {name} with {value} hours worked')

employee_of_month(work_hours)


lista = ['a', 'b', 'c', 'd', 'e']
word = ''.join(lista)
print(word)
for index, letter in enumerate(lista):
    print('this is the index', index)
    print('this is the letter', letter)

def myfunc(a):
    if a == True:
        return 'Hello'

    return "Goodbye"

a = False
myfunc(a)


def myfunc(x,y,z):
    if z is True:
        return x

    return y


myfunc(2,4, False)


def myfunc(a,b):
    return a+b

# Is even
def is_even(a):
    if a % 2 == 0:
        return True

    return False


def is_greater(a,b):
    if a > b:
        return True

    return False
