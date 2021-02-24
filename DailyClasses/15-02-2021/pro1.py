a = 10 # this is a statement
print(a) # print() function call to give standard output-> console

b = 20
c = a + b
print(a," + ",b," = ",c) # variable arguments passing to print

# Fancier Output Formatting
print(f"{a} + {b} = {c}")
name = "Vipul Shah"
print(f"Hello {name},")
print(f"Hello {name:20},")

# print using format
print(str.format("{0} + {1} = {2}", a, b, c))

# str()
print(str(name))

# repr()
print(repr(name))


