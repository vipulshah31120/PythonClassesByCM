list = [2,4,4,6,8,10,12]

# iterating elements of list with for
# in is reserved keyword
for i in list :
    print(i)
    
# we can directly print a list as well
print(list)

# for with slice of list
for i in list[2:] :
    print(i,"\n")
    print("hihihi \n")  #it is in for loop so after every digit 'hihihi' will get printed
    

# for with string
for i in " V i p u l " :
    print(i)


for x in "I still have Hope." :
	if x == "h" :
	  break
	print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 


for x in "I still have Hope." :
	if x == "h" :
		continue
	print(x)
adj = ["A", "This is a", "I have a"]
list1 = ["Cat", "Ball", "Phone"]

for x in adj :
	for y in list1 :
		print(x,y)
	