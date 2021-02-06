matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
print([[row [i] for row in matrix] for i in range(4)])    #gives 4 list
print([[row [i] for row in matrix] for i in range(3)])    #gives 3 lists

print(matrix)
print(list(zip(*matrix)))       #does the same as above row stmnts.