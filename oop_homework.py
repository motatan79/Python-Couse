'''Problem 1
Fill in the Line class methods to accept coordinates as a
pair of tuples and return the slope and distance of the line.'''

class Line:

    def __init__(self, coor1, coor2):

        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2

        print(((x2-x1)**2 + (y2-y1)**2)**0.5)

        return ((x2-x1)**2 + (y2-y1)**2)**0.5


    def slope(self):

        x1, y1 = self.coor1
        x2, y2 = self.coor2

        print((y2 - y1) / (x2 - x1))
        return (y2 - y1) / (x2 - x1)


# EXAMPLE OUTPUT

coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1,coordinate2)

li.distance()
li.slope()


# Problem 2
# Fill in the class

class Cylinder:

    def __init__(self, height=1, radius=1):

        self.height = height
        self.radius = radius

    def volume(self):
        print((self.radius**2) * 3.14 * self.height)
        return self.radius**2 * 3.14 * self.height

    def surface_area(self):
        print(2 * 3.14 * (self.radius**2) + 2*3.14*self.radius*self.height)
        return 2 * 3.14 * (self.radius**2) + 2*3.14*self.radius*self.height


cil = Cylinder(2, 3)
cil.volume()
cil.surface_area()


# For this challenge, create a bank account class that has two attributes:
#
# owner
# balance
# and two methods:
#
# deposit
# withdraw
# As an added requirement, withdrawals may not exceed the available balance.
#
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account can't be overdrawn.

class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance += dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self, wd_amt):

        if self.balance >= wd_amt:
            self.balance -= - wd_amt
            print("Withdrawal accepted")
        else:
            print("Sorry non enough founds")

    def __str__(self):
        return f"Account owner: {self.owner} \nAccount balance: {self.balance}"


acct1 = Account('Jose', 100)
acct2 = Account('Sam', 800)

print(acct2.owner)
print(acct2.balance)
print(acct2)

acct2.deposit(100)
print(acct2)

acct2.withdrawal(600)
print(acct2)





