# iterator : An iterator is an object that contains a countable number of values.
# 1. An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# 2. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

list = ["apple","banana","pineapple","kiwi"]
itr = iter(list)							#iter() method which is used to get an iterator

print(itr.__next__())
print(next(itr))
print(itr.__next__())
print(itr.__next__())


# We can also use a for loop to iterate through an iterable object:
for x in list:
	print(x)