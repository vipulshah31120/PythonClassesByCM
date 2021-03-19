
# we can define a datatype of a variable
name : str = "Vipul \n"
age : int = 20

print(name, age)

# Function annotations are completely optional metadata information about the types used by user-defined functions 
def fun(name : str, age : int = 18):
    print(fun.__annotations__)
    print(name, age)
    if age >= 18:
        print('eligible')
    else : 
        print('not eligible')
fun('cm', 12)


