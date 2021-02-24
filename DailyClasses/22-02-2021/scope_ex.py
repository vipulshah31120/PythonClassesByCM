x = 20  # x has a global (scope_ex.py) level scope

def checking():
	# global x  # you can uncomment 'global x' statement, then checking will use global x and reassign a new value to it otherwise it creates normal local varibale x and use it without affecting global x value
	x = 200
	a = 10  # a has local scope and can only be used inside current function
	print(x)
	def testing():  # inner function -> function inside another function
		i = 1
		print(a)  # a can be accessed here
	# print(i)  # i has a local scope to testing() function, so we cannot access it outside its scope


# print(a)  # we cannot access a here because its scope is local to function checking()
print(x)

checking()  # checking function call

print(x)