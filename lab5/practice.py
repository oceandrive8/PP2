#Exercise 1
import re
txt=open("row.txt")
def a_b(txt):
    sch = r'ab*'
    if re.match(sch, txt):
        return True
    else:
        return False
    
print(a_b("ab"))


#Exercise 2
import re
def a_2b(txt):
    sch = r'ab{2,3}'
    if re.match(sch, txt):
        return True
    else:
        return False
print(a_2b("abbb"))


#Exercise 3
import re
def seq(txt):
    sch = r'[a-z]+_[a-z]+'
    acc= re.findall(sch, txt)
    return acc
print(seq("Hello_how are you"))


#Exercise 4
import re
def seq(txt):
    sch= r'[A-Z][a-z]+'
    acc= re.findall(sch, txt)
    return acc
print(seq("Good How about you"))


#Exercise 5
import re
def match(txt):
    sch= r'a.*b$'
    if re.match(sch, txt):
        return True
    else:
        return False
print(match("agtgsgtsb"))


#Exercise 6
import re
def new(txt):
    new_text= re.sub("[ ,.]", ":", txt)
    return new_text

print(new("Hello, long time no see you"))


#Exercise 7
def snake(txt):
    ph = txt.split('_')
    camel = ph[0] + ''.join(word.capitalize() for word in ph[1:])
    return camel
print(snake("Hi_Barbie_Hi_Ken"))


#Exercise 8
import re

def sp(txt):
    pr = re.findall('[A-Z][^A-Z]*', txt)
    return pr
print(sp("BeautifulThingsDontAskForAttention"))


#Exercise 9
import re

def ins(txt):
    astro= re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
    return astro
print(ins("BeautifulThingsDontAskForAttention"))


#Exercise 10
import re

def camel(txt):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', txt).lower()
print(camel("HealthyAndWealthy"))