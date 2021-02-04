
def after10year(age):
    return age + 10

vipulAge = after10year(20)
print(vipulAge)

cmAge = after10year(12)
print(cmAge)

abc = lambda age : age + 10

vipulGf = abc(20)
print(vipulGf)


# we can pass multiple params as well in lambda expression
sum = lambda a, b : a + b

print(sum(1,2))