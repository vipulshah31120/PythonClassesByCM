#Fibonacci Series

a = 0
b = 1
while a<100 :
    print(a,end=',')        #The keyword argument 'end' can be used to avoid the newline after the output, 
    a,b = b, a+b            #or end the output with a different string
