# When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.

list = [1,2,3,5,76,87,78,85,645,43,32,1,4,665,9]
print(list)
for i, v in enumerate(list):
    print(i,'. ',v)