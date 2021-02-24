# pass statement ->
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Person:
	pass


p1 = Person()
p1.name = "CM"
p1.job = "Developer"
p1.car = "Bekar"

print(p1.__dict__)  # __dict__ is built-in method for checking its internal parameters
#print(p1.Person())
