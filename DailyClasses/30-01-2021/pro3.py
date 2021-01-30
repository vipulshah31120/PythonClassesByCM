# input() is a function used for taking standard input

name = input("What's your name?")
print("hello", name)

# input function always retruns a string
# how we can take an input for number/ integer
# to get an integer we need to parse it into int with help of int()

age = int(input("Hey, What's your age?"))
print("so you are",age,"years old")

# control statements
if age>=18 :
    print("you are eligible")
else :
    print("you are not eligible")
