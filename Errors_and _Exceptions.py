# We use three keywords for this:
# try:this is the block of code to be attempted (may lead to an error).
# except: Block of code will execute in case there is an error try block.
# finally: A final block of code to be executed regardless an error.


def add(n1, n2):
    try:
        # Want to attempt this code
        # May have an error
        print(n1 + n2)
    except TypeError:
        print("No puedes sumar un string y un int")
    else:
        print(n1 + n2)
        print("Lo hiciste muy bien, supiste que hacer")


add(10, 20)

number1 = 10

number2 = input("Please provide a number: ")

# number2 vendrá como un string y dará un TypeError porque no podrá sumar un string y un int

# Ahora vamos a probar abriendo un archivo

try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError:
    print("There was a type error")
except OSError:
    print("Hey you have an OS Error ")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")


ask_for_int()
