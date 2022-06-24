def say_hello():
    print("hello")
    print("are")
    print("you")


say_hello()


def say_hello(name):
    print(f'Hello {name}')


say_hello('Moises')


def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)

print(result)


# Functions with Logic
def even_check(number):
    return number % 2 == 0


even_check(20)
even_check(21)


# Return true if any number is EVEN inside a list


def check_even_list(lista):
    for num in lista:
        if num % 2 == 0:
            # print("Even")
            return True
        else:
            pass
            # print("Odd")
    return False


check_even_list([1, 2, 5])
check_even_list([2, 4, 5])


def check_even_list(lista):
    """return all the even numbers in a list"""

    even_numbers = []
    for num in lista:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            pass

    print(even_numbers)
    return even_numbers


check_even_list([1, 2, 3, 4, 5])
check_even_list([1, 3, 5])

# Tuple unpacking with python Functions

stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]
for ticker, prices in stock_prices:
    print(prices)

work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]
# Decided who is the employee of the year, name and hours worked


def employee_of_the_month(work_hours):

    current_max = 0
    employee_selected = ''
    for name, hour in work_hours:
        if hour > current_max:
            current_max = hour
            employee_selected = name
        else:
            pass
    print(f'Employees of the month is {employee_selected} with {current_max} hours worked')
    return employee_selected, current_max

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]

name, hours = employee_of_the_month(work_hours)
print(name)

# Random
example = [x for x in range(8)]
from random import shuffle
shuffle(example)
print(example)


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


my_list = [' ', 'O', ' ']

print(shuffle_list(my_list))


def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1, or 2")

    return int(guess)

# Ahora para llamar a las otras funciones dentro de la nueva,
# llamo a los argumentos o a las salidas que están en el return


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess")
        print(mylist)


# Initial List
mylist = [' ', 'O', ' ']

# Shuffle list
mixedup_list = shuffle_list(mylist)

# User Guess
guess = player_guess()

# Check Guess
check_guess(my_list, guess)