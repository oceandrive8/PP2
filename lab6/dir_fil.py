#Exercise 1
import os
def ldf(path):
    print("Directories:")
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        if os.path.isfile(os.path.join(path, item)):
            print(item)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for directory in dirs:
            print(os.path.join(root, directory))
        for file in files:
            print(os.path.join(root, file))

path = input("")
ldf(path)

#Exercise 2
import os
def check(path):
    if os.path.exists(path):
        print(f"{path} exists.")
    else:
        print(f"{path} does not exist.")
        return

    if os.access(path, os.R_OK):
        print(f"{path} is readable.")
    else:
        print(f"{path} is not readable.")

    
    if os.access(path, os.W_OK):
        print(f"{path} is writable.")
    else:
        print(f"{path} is not writable.")

    
    if os.access(path, os.X_OK):
        print(f"{path} is executable.")
    else:
        print(f"{path} is not executable.")
path = input("")
check(path)

#Exercise 3
import os
def anlz(path):
    if os.path.exists(path):
        print(f"{path} exists.")
        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print(f"{path} does not exist.")
path = input(" ")

anlz(path)

#Exercise 4
def cl(fname):
    with open(fname, 'r') as file:
            count= sum(1 for line in file)
            print(f"The number of lines in {fname} is: {count}")
fname=input(" ")
cl(fname)


#Exercise 5
def wlif(lst, filename):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(str(item) + '\n')


mylst = ["Merci","Bonjour", "Konbanwa", "Arigato","Oyasumi"]
filename = input("")
wlif(mylst, filename)


#Exercise 6
import string
def generatefiles():
    for lttr in string.ascii_uppercase:
        filename = lttr + ".txt"

generatefiles()


#Exercise 7
def copy(file1, file2):
    f1= open(file1, 'r')
    f2= open(file2, 'w')

    cont= f1.read()
    f2.write(cont)

    f1.close()
    f2.close()


file1= input("")
file2= input("")

copy(file1, file2)

#Exercise 8
import os
def delete(path):
    if not os.path.exists(path):
        print(f"{path} does not exist.")
        return
    if not os.access(path, os.W_OK):
        print(f"{path} is not accesable.")
        return

    os.remove(path)
    
path = input("")

delete(path)





            




