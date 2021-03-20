# When looping through a sequence, the position index and corresponding value can be retrieved at the same -
#time using the enumerate() function.

list1 = [1,2,3,5,76,87,78,85,645,43,32,1,4,665,9]
print(list1)
for i, v in enumerate(list1):
    print(i,'. ',v)


x = ('Rome', 'Zurich', 'Sweden', 'Ibiza') 	#The enumerate() function takes a collection (e.g. a tuple) and returns it as an enumerate object.
y = enumerate(x)

print(list(y))