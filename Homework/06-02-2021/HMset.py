basket = {'apple','orange','grapes', 'banana', 'apple', 'watermelon'}
print(basket)
print(type(basket))

print('orange' in basket)       #True
print('pear' in basket)         #False

a = set('abracadabra')
b = set('alacazam')

print(a)                        # unique letters in a
print(a-b)                      # letters in a but not in b
print(a | b)                    # letters in a or b or both
print(a & b)                    # letters in both a and b
print(a ^ b)                    # letters in a or b but not both

a = {x for x in 'abracadabra' if x not in 'abc' }           #set comprehensions are also supported 
print(a)

print(sorted(basket))
