#Exercise 1
def recipe():
   gram=float(input())
   print(gram/28.3495231)

recipe()
"""
by the way the formula is ounces=grams/28.3495231.
converting grams to ounces
"""


#Exercise 2
def temp():
   fah=float(input())
   cel=(5/9)*(fah-32)
   print(cel)
temp()


#Exercise 3
def solve(numheads, numlegs):
   rab=(numlegs-(numheads*2))/2
   chick=numheads-rab
   print("rabbits: ", rab)
   print("chickens: ",chick)
solve(35,94)

#Exercise 4
def prime(n):

    if n < 2:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [n for n in numbers if prime(n)]
numbers = list(map(int,input().split()))
print(filter_prime(numbers))


#Exercise 5
def permu(word):
    if len(word) == 0:
        return ['']
    
    perms = []
    for i in range(len(word)):
        f_ch = word[i]
        oth_ch = word[:i] + word[i+1:]
        for perm in permu(oth_ch):
            perms.append(f_ch + perm)
    
    return perms

def print_permutations(word):
    perms = permu(word)
    for perm in perms:
        print(perm)

word = input("Enter a string: ")
print_permutations(word)


#Exercise 6
def revs(ph):
    words = ph.split()
    revw = reversed(words)
    revs = ' '.join(revw)
    return revs


ph = input("")
reverse=revs(ph)
print(ph,"->",reverse)


#Exercise 7
def has_33(list2):
    for i in range(len(list2) - 1):
        if list2[i] == 3 and list2[i+1] == 3:
            return True
    return False

print(has_33([1,0,3,4]))


#Exercise 8
def spy_game(nums):
    pos_0 = None
    pos_7 = None
    for i, num in enumerate(nums):
        if num == 0:
            pos_0 = i
        elif num == 7:
            pos_7 = i
        if pos_0 is not None and pos_7 is not None and pos_0 < pos_7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7]))  
print(spy_game([1,7,2,0,4,5,0])) 


#Exercise 9
import math
def volume(rad):
    V=(4/3)*math.pi*(rad**3)
    return V
print(volume(4))


#Exercise 10
def dup():
    list1=[]
    n = int(input("Number of elements: "))
    for i in range(n):
        a = int(input())
        list1.append(a)

    print("The list after", list1)
    

    res = []
    [res.append(x) for x in list1 if x not in res]
    print("List with unique elements: ",str(res))
dup()


#Exercise 11
def palindrome():
    att=input("")
    ocdr=att [::-1]
    if att==ocdr:
        print("Yes, palindrome!")
    else:
        print("No palindrome")
palindrome()


#Exercise 12
def histogram(nums):
    for num in nums:
        print('*' * num)


histogram([4, 9, 7])


#Exercise 13
def game():
    print("Hello, what's your name?")
    name = input("")
    print("Well, " + name + ", I am thinking of a number between 1 and 20 \nTake a guess.")
    
    count = 0  
    
    while True:  
        num = int(input())
        count += 1  
        
        if num < 19:
            print("Your guess is too low. \nTake a guess.")
        elif num > 19:
            print("Your guess is too high. \nTake a guess.")
        else:
            print("Good job, " + name + "! You guessed my number in " + str(count) + " guesses!")
            break  
game()



   
      

   

