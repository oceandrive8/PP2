#Exercise 1
import math
n=int(input())
list=[]
for i in range(n):
    i=int(input())
    list.append(i)
multi=math.prod(list)
print(multi)


#Exercise 2
text=input("")
upper=sum(1 for char in text if text.isupper())
lower=sum(1 for char in text if text.islower())
print(upper, lower)


#Exercise 3
def pal(text):
    text= ''.join(char.lower() for char in text if char.isalnum())
    
    return text== text[::-1]

phrase=input("")
if pal(phrase):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


#Exercise 4
import time
import math

def sqr(num, mil):
    time.sleep(mil / 1000)
    res= math.sqrt(num)
    print(f"Square root of {num} after {mil} milliseconds is {res}")

num=25100
mil=2123
sqr(num, mil)



#Exercise 5
tuple=(True, True, False, True)
check=all(tuple)
print(check)
if(check==True):
    print("All elements are true")
else:
    print("Not all elements true")


