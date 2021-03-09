name = input("Enter your naam: ")
print("Hello",name)

age = int(input("Enter your age: "))
#print(type(age))
try : 
	if age<18 : 
		raise Exception("Red Alert")

except :
	print("Under Age")

else :
	print("Eligible")

finally :
	print("Tata Bye Bye")

