#  Almost everything in Python is an object, with its properties and methods.
#  A Class is like an object constructor, or a "blueprint" for creating objects.

class Myclass1 :
	x=5
p1=Myclass1()		#Creating an object named p1, and printing the value of x:
print(p1.x)

class Student :
	def __init__(student,name,age,college) :
		student.name = name
		student.age = age
		student.college = college
s1=Student('Vipul', 22, 'GTBIT')

print(s1.name)
print(s1.age)
print(s1.college)


class Person:
	def __init__(self, name, age) :
		self.name = name
		self.age = age


p1 = Person("Tom", 45)
print(p1.name)
print(p1.age)


class Person2:
	def __init__(self, section, rollNo) :
		self.section = section
		self.rollNo = rollNo

	def myfunc(self) :
		mine = "My section is " + self.section, "and Roll Number is " + self.rollNo	  

		return mine


p2 = Person2("IT-3", "04076803117")
# print(p2.section)
print(p2.myfunc())
print(p2.section)
print(p2.rollNo)



class Laptop :
	def __init__(self, ram, storage) :
		self.ram = ram
		self.storage = storage

	def company(self) :
		print("RAM : ", self.ram)
		print("Storage space : ", self.storage)	

l1 = Laptop("8 GB", "1 TB")
l2 = Laptop("10 GB", "2TB")
print(l1.ram)
print(l1.storage)		

print(l2.ram)
print(l2.storage)

l1.company()
l2.company()


class Home :
	def __init__(object, item1, item2) :
		object.item1 = item1
		object.item2 = item2

	def decor(abc) :
		print("No. of Doors :" + abc.item1)
		print("No. of Beds :" + abc.item2)

h1 = Home("10", "4")
h1.decor()
