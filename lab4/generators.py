#Exercise 1
n=int(input("Some N:"))
gene=(i**2 for i in range(n+1))
for i in gene:
    print(i)


#Exercise 2
n=int(input("Some n:"))
gene=(i for i in range(0,n+1) if i%2==0)
list=[]
for i in gene:
    list.append(i)

print(','.join(str(i) for i in list ))



#Exercise 3
n=int(input("Some n:"))
def gen(n):
   gene=(i for i in range(0,n+1) if (i%3==0 and i%4==0)) 
   for i in gene:
       print(i)
gen(n)


#Exercise 4
a=int(input("Some a:"))
b=int(input("Some b:"))
def sq(a,b):
    for i in range(a,b+1):
        yield i**2
        
for i in sq(a,b):
   print(i) 



#Exercise 5
n=int(input("Some n:"))
def dow(i):
    while i>=0:
        yield i
        i-=1

for  u in dow(n):
    print(u)
