def calculateInterest(r):
    """I am a documentation string.
    
    you can read a documentation string by calling parameter __doc__ with the name of a function.
    
    for example:
    
    to call current function's documentation string
    
    calculateInterest.__doc__
    """
    return lambda p, t: p * r * t / 100

pnbInterest = calculateInterest(10)
sbiInterest = calculateInterest(9)

vipulInterest = pnbInterest(100, 2)
vipulInterest2 = sbiInterest(200, 2)
cmInterest = sbiInterest(100, 2)

print('Vipul pay : ', vipulInterest)
print('CM pay : ', cmInterest)
print('Vipul pay 2 : ', vipulInterest2)

print(calculateInterest.__doc__)