def function1(*args):
    print(args)


def fun2(a, *args):
    print(a)
    print(args)


fun2('cm', 2,3,5)
function1(1,2,3)