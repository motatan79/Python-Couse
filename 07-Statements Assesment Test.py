# Use for, .split(), and if to create a Statement that will
# print out words that start with 's':
st = 'Sam Print only the words that start with s in this sentence'

for word in st.split():
    if word[0].lower() == 's':
        print(word)

# List Comprehension
mylist = [word for word in st.split() if word[0] == 's']
print(mylist)

# Use range() to print all the even numbers from 0 to 10.
even = [x for x in range(0, 11, 2)]
print(even)

# Use a List Comprehension to create a list of all
# numbers between 1 and 50 that are divisible by 3.

three = [x for x in range(1, 51) if x % 3 == 0]
print(three)

# Go through the string below and if the length of a word
# is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for word in st.split( ):
    if len(word) % 2 == 0:
        print(word + ' is even')

word_even = [(word, ' is even') for word in st.split() if len(word) % 2 == 0]
print(word_even)

#Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which
# are multiples of both three and five print "FizzBuzz".

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print(number, 'FizzBuzz')
    elif number % 3 == 0:
        print(number, "Fizz")
    elif number % 5 == 0:
        print(number, 'Buzz')
    else:
        print(number)

# Use List Comprehension to create a list of the first letters of
# every word in the string below:

st = 'Create a list of the first letters of every word in this string'

mylist = [word[0] for word in st.split()]
print(mylist)







