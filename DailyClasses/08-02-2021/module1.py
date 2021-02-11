# A module is a file containing Python definitions and statements.
# The file name is the module name with the suffix .py appended.
# Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

import module2 as m2
import module3 as m3
import prime_checker as m4
print(__name__)

LIMIT = 100
a = 0
b = 1
while a<100:
    print(a,end=', ')
    a, b = b, a+b   # first calculate RHS then assign these values to LHS 
    
print()
a = 0
b = 1
while a<100:
    print(a, end=', ')
    temp = a
    a = b
    b = temp + b
print()


answer = m2.checkOddEven(6)
print(answer)

squares = m3.square(4)
print(squares)

prime = m4.isprime(7)
print(prime)