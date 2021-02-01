# funtion : Functions are "self contained" modules of code that accomplish a specific task.
# 1. Functions usually "take in" data, process it, and "return" a result.
# 2. Once a function is written, it can be used over and over and over again.
# 3. Functions can be "called" from the inside of other functions.

def doSomething() :
    print("Hey vipul, how's girlfriend??")
    print("Vipul : Ooper wale ki dua hai bsss...")

doSomething()

# Default Argument Values

def doSomethingByDefault(name="Vipul", age=12) :
    print(name,"is",age,"years old")

doSomethingByDefault(age=24)

# interest calculation

def a(p, t, r=10) :
    return p * r * t / 100;

print(a(p=10000, r=12, t=2))