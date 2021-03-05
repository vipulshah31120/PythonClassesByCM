# list : Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

family = ["Pita Ji","Mata Ji","Bhrata Ji","Behan Ji","Dada Ji","Dadi Ji","Me","and 4 others"]
print(family)

# there many function for list:
# append(), extend(), insert(), remove(), pop(), clear(), index(), count(), sort(), reverse(), copy().

# Using Lists as Stacks
family.append("pahli wali")
family.append("dosri wali")
print(family)

family.pop()
print("after pop: ")
print(family)

family.pop()
print("after pop: ")
print(family)

# Using Lists as Queues
# While appends and pops from the end of list are fast, doing inserts or pops from the beginning of a list is slow (because all of the other elements have to be shifted by one).
# To implement a queue, use collections.deque which was designed to have fast appends and pops from both ends.

from collections import deque
gfQue = deque(["Muskan","Simran"])
gfQue.append("Aishwarya")

print(gfQue)

gfQue.pop();
print("pop");
print(gfQue)

gfQue.popleft();
print("popleft");
print(gfQue)

fruits = ["apple", "banana", "cherry" ]
x, y, z = fruits
print(x)	# apple
print(y)	# banana
print(z)	# cherry
