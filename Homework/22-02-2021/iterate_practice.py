list = ["I", "still", "have", "hope"]
itr1 = iter(list)

print(itr1.__next__())	# 1st syntax
print(next(itr1))		# 2nd syntax
print(itr1.__next__())
print(next(itr1))

str1 = "Salvatores"
itr2 = iter(str1)	# iter() method which is used to get an iterator

print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))
print(next(itr2))

for x in str1 :
	print(x)


for x in list :
	print(x)


class Student :
	def __iter__(self) :
		self.a = 1
		return self

	def __next__(self) :
		x = self.a 
		self.a += 1
		return x

s1 = Student()
itr3 = iter(s1)

print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))


class Vehicle :
	def __iter__(self) :
		self.a = 2
		return self

	def __next__(self) :
		x = self.a
		self.a *= 2
		return x

v1 = Vehicle()
itr4 = iter(v1)

print(next(itr4))
print(next(itr4))
print(next(itr4))
print(next(itr4))













