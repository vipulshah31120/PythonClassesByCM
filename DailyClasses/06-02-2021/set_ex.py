# Python also includes a data type for sets. A set is an unordered collection with 'no' duplicate elements

set_gf = {"simran","priyanka","simran","rani"}
print(set_gf)
print(len(set_gf))

# set comprehension
set_of_char = {x for x in 'simran' if x not in 'ai'}
print(set_of_char)


set1 = {"Alpha", "Beta", "Gamma", "Theta", "Tan"}
set2 = {"Sin", "Cos", "Tan", "Cot"}

set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

x = {"Apple","Orange", "Papaya"}
y = {"Jordan", "Curry", "Papaya"}

z = x.intersection(y)
print(z)

z = x.intersection_update(y) 	#Not Working
print(z)

z = x.symmetric_difference(y)
print(z)

x.update(y)		#Not Working
print(x)