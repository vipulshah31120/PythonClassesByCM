# List Comprehensions
square = []
for x in range(1,16):
    square.append(x**2)

print(square)

# alternate 
squares = [x**2 for x in range(1, 16)]
print(squares)