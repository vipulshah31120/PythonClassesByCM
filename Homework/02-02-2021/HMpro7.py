fruits = ['orange' , 'apple', 'banana', 'kiwi','grapes', 'apple']

print(fruits.count('apple'))

fruits.append('watermelon')     #first append then print it
print(fruits)

print(fruits.index('kiwi'))

print(fruits.index('apple', 2))  # Find next apple starting a position 2

fruits.sort()
print(fruits)

fruits.pop()                    #blank () will pop the last element
print(fruits)

fruits.pop(2)                    #will pop the 2nd element acc. to list
print(fruits)
