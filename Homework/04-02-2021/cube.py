cube = []
for x in range(1,16) :
    cube.append(x**3)

print(cube)

#alternate
cube = [x**3 for x in range(1,16)]
print(cube)