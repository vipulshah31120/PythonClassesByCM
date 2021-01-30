word='mexico'

print(word[0])
print(word[-2])
print(word[0:2])

print(word[:2]+word[2:]) #to check how the start is always included, and the end always excluded.

print('T' + word[1:])

cubes = [1, 8, 27, 65, 125]
cubes[3]= 64
print(cubes)

a=['x' ,'y', 'z']
n=[1,2,3,4]
x=[a,n]
print(x)
print(x[1][3])          #to print 3rd value from 1st list