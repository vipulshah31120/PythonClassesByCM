#An array is a special variable, which can hold more than one value at a time.
cars=['BMW','AUDI','Buggati','McLaren']
x=cars[2]
print(x)
print(cars[2])

cars[2]='Volkswagen'
print(cars)

x=len(cars)
print(x)

for x in cars :
	print(x)

cars.append('Honda')
print(cars)

cars.pop(2)
print(cars)

cars.remove('AUDI')
print(cars)

