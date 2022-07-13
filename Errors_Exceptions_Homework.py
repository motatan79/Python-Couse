# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except TypeError:
    print("You can power an string")


# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print
# 'All Done.'

try:
    x = 5
    y = 0
    z = x/y
    print(z)
except ZeroDivisionError:
    print("You can divide by zero")
finally:
    print("All Done")


# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except,
# else block to account for incorrect inputs.

def ask():
    while True:
        try:
            n = int(input("Please provide an integer: "))
        except ValueError:
            print("That is not a number! \n")
            continue
        else:
            print("Nice jobs, thank you!")
            break

    print("Your number square is: ", n**2)

ask()
