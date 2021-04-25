#Fibonacci Series

a = 0
b = 1
while a<100 :
    print(a,end=',')        #The keyword argument 'end' can be used to avoid the newline  
    a,b = b, a+b            #after the output, or end the output with a different string
