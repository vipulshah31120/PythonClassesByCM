def isPrime(n) :
    for i in range (2,n) :
        if n%i==0:
            print(n,'is divisible by',i)
            return False
    return True


print('Prime' if isPrime(53) else 'Not Prime')

#1------53
# 2----52
 
def isAgreater(a, b):
    return a > b
    
print(isAgreater(2,3))
print(isAgreater(5,3))