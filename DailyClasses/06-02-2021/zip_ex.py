cars = ['ferarri', 'mazerati', 'lambo', 'toyota']
bikes = ['kawasaki', 'yossung', 'harley', 'hasqverna']

for c , b in zip(cars, bikes) :
    print(f'i have {c} and {b}')
    
print('i have {0} and {1}'.format(c,b))     # {0} & {1} has the value of format