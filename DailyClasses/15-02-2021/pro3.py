def table(n) :
	for i in range (1,11) :
		print(f"{n:2} * {i:2} = {n*i}")

table(19)  


x=5
x+=3
print(x)

x=8
x//=4
print(x)

x=6
y=4
if x>=y:
	print("x>y")

x=5
print(x>4 and x<10)
print(x>4 and x>10)
print(x>4 or x>10)

x=['vipul','shubham']
print('vipul' in x)
print('riya' in x)

fruits = ['apple','banana','mango','cherry']
i=0
while i<len(fruits):
	print(fruits[i])
	i=i+1

[print(x) for x in fruits]

newlist=[x.upper()for x in fruits]
print(newlist)

a=2
b=5
c=a+b
print(a,"+",b,"=",c)
print(str.format("{0}+{1}={2}",a,b,c))

name="Akash"
print(str(name)) 	#Important
print(repr(name))

section="IT-3"
marks=56.98765
Roll="04076803117"
print(Roll)
print(f"{'name':7} {name}")
print(f"{'section':5} {section}")
print(f"{'marks':7} {marks:.3f}")