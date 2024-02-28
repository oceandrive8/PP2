#Exercise 1
import re
def a_b(text):
    sch = r'ab*'
    if re.match(sch, text):
        return True
    else:
        return False
    
print(a_b("ab"))



#Exercise 2
import re
def a_2b(text):
    sch = r'ab{2,3}'
    if re.match(sch, text):
        return True
    else:
        return False
print(a_2b("abbb"))



#Exercise 3
import re
def seq(text):
    sch = r'[a-z]+_[a-z]+'
    acc= re.findall(sch, text)
    return acc
print(seq("Hello_how are you"))



#Exercise 4
import re
def seq(text):
    sch= r'[A-Z][a-z]+'
    acc= re.findall(sch, text)
    return acc
print(seq("Good How about you"))



#Exercise 5
import re
def match(text):
    sch= r'a.*b$'
    if re.match(sch, text):
        return True
    else:
        return False
print(match("agtgsgtsb"))



#Exercise 6
import re
def new(text):
    new_text= re.sub("[ ,.]", ":", text)
    return new_text

print(new("Hello, long time no see you"))



#Exercise 7
import re
def snake(case):
    ph = case.split('_')
    camel = ph[0] + ''.join(word.capitalize() for word in ph[1:])
    return camel
print(snake("Hi_Barbie_Hi_Ken"))



#Exercise 8
import re
def sp(text):
    pr = re.findall('[A-Z][^A-Z]*', text)
    return pr
print(sp("BeautifulThingsDontAskForAttention"))



#Exercise 9
import re
def ins(text):
    astro= re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return astro
print(ins("BeautifulThingsDontAskForAttention"))



#Exercise 10
import re
def camel(case):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', case).lower()
print(camel("HealthyAndWealthy"))



