print("Kamaaal hai ji..., try CTRL+B")
print("HIHIHIHI")

x = lambda a : a + 20 
print(x(22))

x = lambda a,b : a*b
print(x(34,56))

x = lambda a,b,c : a+b*c
print(x(2,4,5))

def myfunc(n) :
	return lambda a : a*n

mydoubler = myfunc(4)	# n=4
print(mydoubler(5)) 	# a=5

mytripler = myfunc(6)	#n=6
print(mytripler(8))		#n=8

#Calculating Simple Interest
def SI(r) :
	return lambda p,t : p*r*t/100

CalculateSI=SI(10)
SIforme=CalculateSI(100,4)
print(SIforme)

for n in range(1,101) :
	if n%3==0 and n%5==0 :
		print("FizzBuzz")

	elif n%3==0 :
		print("Fizz")

	elif n%5==0 :
		print("Buzz")

	else :
		print(n)


def FizzBuzz(n) :
	if n%3==0 and n%5==0 :
		print("FizzBuzz")

	elif n%3==0 :
		print("Fizz")

	elif n%5==0 :
		print("Buzz")

	else :
		print(n)

FizzBuzz(100)




