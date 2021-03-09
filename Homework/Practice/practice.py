#1
x = "Awsome"

def Mydef() :
	print("I am " + x)

Mydef()



#2	Using same variable
y = "Awsome"

def Myfunc() :
	y = "God"
	print("I am " + y)

Myfunc()

print("I am " + y)



import random		# prints the random no. in the given range 
print(random.randrange(1, 10))




a = "   I have, a Dream.   "
print(a.strip())
print(a.split(","))




age = 22
n = "My name is Vipul and i'm {} years old."
print(n.format(age))



quantity = 20
from1 = "Delhi"
to = "Mumbai"

b = "I want to transfer {0} Kg rice from {1} to {2}."
# b = "I want to transfer {} Kg rice from {} to {}."
print(b.format(quantity, from1, to)) 



c = "I still \rhave Hope"
print(c)


list1 = ["Coke", "Fanta", "Limca", "Pepsi"]
list1[1:2] = ["ThumbsUp"]
print(list1)


str = "this2009";  # No space in this string
print (str.isalnum())

str = "this is string example....wow!!!";
print (str.isalnum())

str = "qA2"
print (str.isalpha())

def fun1(s):
    for i in range(len(s)):
        if(s[i].isalnum()):
            return True;
            break;
    return False;
print(fun1("qA2"))
        
def fun2(s):
    for i in range(len(s)):
        if(s[i].isalpha()):
            return True;
            break;
    return False;

print(fun2("qA2"))

def fun3(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            return True;
            break;
    return False;

print(fun3("qA2"))

def fun4(s):
    for i in range(len(s)):
        if(s[i].islower()):
            return True;
            break;
    return False; 

print(fun4("qA2"))
     
def fun5(s):
    for i in range(len(s)):
        if(s[i].isupper()):
            return True;
            break;
    return False;

print(fun5("qA2"))
 
# String Validators in Python - Hacker Rank Solution END 
    
#if __name__ == '__main__':
    #s = "qA2"
    
    # String Validators in Python - Hacker Rank Solution START
    #flagalphanum = fun1(s)
    #alphabetical = fun2(s)
    #digits = fun3(s)
    #lowercase = fun4(s)
   #uppercase = fun5(s)
   #print(flagalphanum)
    #print(alphabetical)
    #print(lowercase)
    #print(uppercase)

width = 15
print ('HackerRank'.ljust(width,'-'))

import camelcase
c = camelcase.CamelCase()

s = "shubham"
print(c.hump(s))


import re
v = "Advanced compneuter networks in IT"
v1 = re.search("^Advanced.*IT", v)
 
if v1 :
	print("Found")
else :
	print("Not Found")

v2 = re.findall("ne", v)
print(v2)

v3 = re.search("\s", v)
print("The first white-space character is located in position:",v3.start())

v4 = re.split("\s", v)
print(v4)

v5 = re.sub("\s","SO", v)
print(v5)

