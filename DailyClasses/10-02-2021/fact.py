def fact(x) :
    for i in range (x-1, 0, -1) :
        x = x*i 
        print(i, x)
    return x

print(fact(5))