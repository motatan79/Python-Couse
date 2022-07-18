"""
A Very Simple Script
"""

from random import shuffle


def myfunc():
    """
    A simple function
    """
    first = 1
    second = 2
    print(first)
    print(second)


myfunc()

stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item)

price = [price + 0.1 * price for comp, price in stock_prices]
print(price)

work_hours = [('Abby', 100), ('Billy', 4000), ('Cassie', 800)]


def employee_check(work_hours):
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    return employee_of_month, current_max


result = employee_check(work_hours)
print(result)

name, hours = employee_check(work_hours)
print(name)


mylist = [i for i in range(8)]
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


result = shuffle_list(mylist)


mylist = [' ', 'O', ' ']

def player_guess():

    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0, 1 or 2 ")

    return int(guess)

player_guess()

# Function interacting each other
def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)

# Ahora para correr el programa

# Initial list
mylist = [' ', 'O', ' ']
# Shuffle list
mixedup_list = shuffle_list(mylist)
# User guess
guess = player_guess()
# Check guess
check_guess(mixedup_list, guess)
