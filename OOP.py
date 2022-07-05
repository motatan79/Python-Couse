# Object Oriented Programming

# Class keyword is to create a user defined objects

class Dog:
    # Aquí podemos colocar todas las características comunes para los atributos dentro de la clase
    # no se usa la palabra "self" porque será True a pesar de la instancia que sea llamada
    # Class object attribute
    # Same for any instance of a class
    species = 'mammal'

    # We create __init__ method
    # self connects this method to the instance of the class
    # and it allows refer to itself
    def __init__(self, breed, name, spots):

        # Attributes
        # We take in the argument , in this case "breed"
        # Assign it using self.attribute_name
        self.breed = breed
        self.name = name
        self.spots = spots

    # METHODS
    # Methods are essentially functions defined inside the body of the class
    # ,and they're used to performing operations that sometimes utilize the actual attributes of the object
    # we created.
    # Methods is a function that is inside a class that will actually work with
    # the object in some way.
    # Operations/actions ---> Methods
    def bark(self, number):
        print("WOOF! My name is {} and the number is {}".format(self.name, number))

# Para crear una variable, es una instancia de la clase
# y tenemos que pasarle el parámetro de la raza porque así lo
# definimos cuando creamos el método
my_dog = Dog(breed='Lab', name='Sammy', spots=False)

print(my_dog.breed)
print(my_dog.name)
print(my_dog.spots)

# Methods will need to be executed, and that why we include ()
my_dog.bark(3)


# ------------------------------------------

class Circle:

    # Class Object attribute
    pi = 3.14

    def __init__(self, radius= 1):

        self.radius = radius
        self.area = radius*radius * Circle.pi

    # Method
    def get_circumference(self):
        # COmo pi es una class object attribute, lo podemos llamar de dos maneras
        # self.pi o haciendo referencia al nombre de la clase Circle.pi

        print(self.radius* Circle.pi * 2)


# Ahora vamos a crear una instancia de esa clase
my_circle = Circle(30)

print(my_circle.pi)
print(my_circle.radius)
my_circle.get_circumference()
print(my_circle.area)

# INHERITANCE AND POLYMORPHISM
# Inheritance is basically a way to form new classes using classes that already
# been defined


class Animal:

    def __init__(self):
        print("ANIMAL CREATED")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I'm eating")

# Podemos crear otra clase considerando algunos parámetros de otra clase creada previamente
class Dog(Animal):

    def __init__(self):
        # Porque estoy heredando de la clase Animal que cree previamente
        Animal.__init__(self)
        print("Dog Created")

    # Si queremos podemos reescribir los métodos de la clase heredada pero tenemos que colocarle el mismo nombre
    def who_am_i(self):
        print("I'm a dog!")
    # También podemos agregar métodos
    def bark(self):
        print("WOOF!")
my_dog = Dog()
my_dog.who_am_i()
my_dog.bark()
my_dog.eat()

# Special Methods

class Book:

    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    # Para usar las funciones predefinidas por Python tengo que crear una función
    def __str__(self):
        return f'{self.title} by {self.author}'

    # para len
    def __len__(self):
        return self.pages

    # cuando quieres que algunas cosas ocurran al borrar una variable
    def __del__(self):
        print("A book object has been deleted")


b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))
del b
