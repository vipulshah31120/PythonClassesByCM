
num = [2, 4, 56, 774, 875, 2, 96 ,785328, 55]

evens = list(filter(lambda n : n%2==0, num ))
print(evens)

doubles = list(map(lambda n : n*2, evens))
print(doubles)


from functools import reduce
sum1 = reduce(lambda a,b : a+b, doubles)
print(sum1) 




