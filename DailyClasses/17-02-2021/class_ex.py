name = "CMPundhir"
age = 12

print(type(name))
print(type(age))

# python is object oriented language
# Almost everything in Python is an object, with its properties and methods.

class Student:
	name = "Vipul"

student1 = Student()
student1.age = 20
print(student1.name)
print(student1.age)


# in python built-in functions -> __functionname__
# all built-in functions starts with double underscore -> __

class Employee:
	name = "Viupl" 		#it's an variable of class
	def __init__(self, n):
		self.name = name 	#it is an variable of object


emp1 = Employee("CMPundhir")
print(emp1.name)			#calling variable of object
print(Employee.name)		#calling variable of class
Employee.name = "Ramu"
print(Employee.name)


