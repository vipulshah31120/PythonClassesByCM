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

