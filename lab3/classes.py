#Exercise 1
class stringss:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

word=stringss()
word.getString()
word.printString()


#Exercise 2
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2


sh = Shape()
print(sh.area())

sq = Square(5)
print(sq.area()) 


#Exercise 3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
re=Rectangle(3,4)
print(re.area())


#Exercise 4
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

#for example having these points:
p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show()  
p2.show()  

distance = p1.dist(p2)
print("Distance:", distance)  


#Exercise 5
class bank:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print(f"Withdrawal unsuccessful.")

acc=bank("Ayala", 8000)
print(f"{acc.owner}'s initial balance: {acc.balance}")

acc.deposit(500)
acc.withdraw(1500)    


#Exercise 6
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return list(filter(lambda x: prime(x), numbers))

numbers = list(map(int, input().split()))
print(filter_prime(numbers))





