#A tuple consists of a number of values separated by commas
t = 12345, 6789, "vipul" 
print (t[0])
print (t[2])

t = (12345, 6789, "vipul")

# Tuples may be nested:
u = t, (1,2,3,4)
print(u)

# Tuples are immutable
#t[0] = 55
print(t)               #TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1,2,3,4,], [5,6,7,8,9])
print(v)
print(t,v)