#Exercise 1
import math
n=int(input("Input degree:"))
r=math.radians(n)
print("Output radian:", r)


#Exercise 2
h=float(input("Height:"))
fv=float(input("First value:"))
sv=float(input("Second value:"))
Area=1/2*(fv+sv)*h
print("Area:", Area)


#Exercise 3
import math
n=float(input("Input number of sides:"))
l=float(input("Input the length of a side:"))
a=l/(2*math.tan(180/n)) #apothem
AreA=(n*l*a)/2
print("Area:", AreA)


#Exercise 4
b=float(input("Length of base:"))
h=float(input("Height of parallelogram:"))
Area=b*h
print("Expected Output:", Area)
