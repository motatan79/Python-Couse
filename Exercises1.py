# Functions # 1: print Hello World

def myfunc(word):
    lista = []

    for a, b in enumerate(word):
        if (a+1) % 2 == 0:
            lista.append(b.upper())
        else:
            lista.append(b.lower())

    return "".join(lista)

myfunc('Antrophomorphism')


# LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
# but returns the greater if one or both numbers are odd

def lesser_of_two_evens(a, b):

    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            print(a)
            return a
        else:
            print(b)
            return b
    else:
        if a > b:
            print(a)
            return a
        else:
            print(b)
            return b


lesser_of_two_evens(2, 4)

lesser_of_two_evens(2, 5)

# ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
def animal_crackers(text):
    a = [x for x in text.split()]
    if a[0][0] == a[1][0]:
        print(True)
    else:
        print(False)

animal_crackers('Levelheaded Llama')
animal_crackers('Crazy Kangaroo')

# MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
def makes_twenty(n1, n2):
    if n1 == 20 or n2 == 20:
        print(True)
    elif n1 + n2 == 20:
        print(True)
    else:
        print(False)


makes_twenty(20,10)
makes_twenty(2,3)

# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    letters = []
    for x,y in enumerate(name):
        if x == 0 or x == 3:
            letters.append(y.upper())
        else:
            letters.append(y)
    print("".join(letters))

old_macdonald('macdonald')

# MASTER YODA: Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    a = [x for x in text.split()]
    print(" ".join(a[::-1]))


master_yoda('I am home')
master_yoda('We are ready')


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
# def almost_there(n):


# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
def has_33(nums):
    a = [str(x) for x in nums]
    b = "".join(a)
    print('33' in b)


has_33([1, 3, 1, 3])
has_33([1, 3, 3])

# PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    lista = []
    for b in text:
        lista.append(b*3)

    print("".join(lista))


paper_doll('Hello')
paper_doll('Mississippi')

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
# exceeds 21, return 'BUST'

'''def blackjack(a,b,c):
    suma = a+b+c
    if b == 11 or a == 11 or c == 11 and suma > 21:
        test = suma - 10
        if test > 21:
            print
        if test > 21:
            print('BUST')
    elif suma <:
        print(suma)


blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)'''

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
def summer_69(arr):
    if 6 not in arr:
        print(sum(arr))
    elif 6 in arr:
        for i in arr:
            if i == 6 or i == 9:
                a = arr.index(6)
                b = (arr.index(9)) + 1
                lista = arr[a:b]
                total = sum(arr) - sum(lista)
        print(total)


summer_69([1, 3, 5])
summer_69([4, 5, 6, 7, 8, 9])
summer_69([2, 1, 6, 9, 11])
summer_69([2,4,5,250,6,1000,9])


# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    a = [str(x) for x in nums]
    b = "".join(a)
    print('007' in b)

spy_game([1, 2, 4, 0, 0, 7, 5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,2,0,4,5,0])

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):

    primes = []
    primes2 = [2, 3, 5, 7]
    for i in range(2,num+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            primes.append(i)
    print(len(primes + primes2))

count_primes(100)
count_primes(103)

# Write a function that computes the volume of a sphere given its radius.
def vol(rad):
    print((4/3) * ((3.14)*(rad**3)))
    return (4/3)*(3.14)*(rad**3)

vol(2)

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num,low,high):
    print(num in range(low, high+1))
    #return num in range(low, high+1)

    if num in range(low, high+1):
        print(f'{num} is in the range between {low} and {high}')
    else:
        print('not in range')

ran_check(5,2,7)
ran_check(8,1,5)

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
def up_low(s):
    lowercase = 0
    uppercase = 0

    for i in s:
        if i.isupper():
            uppercase += 1
        elif i.islower():
            lowercase += 1
        else:
            pass
    print(uppercase)
    print(lowercase)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

# Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list(lst):
    '''print(list(set(lst)))
    return list(set(lst))'''
    x = []
    for number in lst:
        if number not in x:
            x.append(number)
    print(x)
    return x


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])

# Write a Python function to multiply all the numbers in a list.
def multiply(numbers):
    result = 1
    for num in numbers:
        result *= num
    print(result)

multiply([1,2,3,-4])
multiply([1,2,3,4,-10])


# Write a Python function that checks whether a word or phrase is palindrome or not.
def palindrome(s):
    a = s.replace(" ", "")
    print(a)
    print(a == a[::-1])
    print(a == reversed(a))
    return a == a[::-1]
s = 'helleh'
palindrome(s)

s = 'nurses run'
palindrome(s)

# Write a Python function to check whether a string is pangram or not.
# (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str2 = str1.lower()
    phrase = sorted(list(set(str2.replace(" ", ""))))
    phrase = "".join(phrase)
    print(phrase == alphabet)
    return phrase == alphabet

ispangram("The quick brown fox jumps over the lazy dog")

