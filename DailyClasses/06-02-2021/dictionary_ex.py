# It is best to think of a dictionary as a set of  {key : value pairs} , 
#with the requirement that the keys are unique (within one dictionary).


person = {'first_name':'Vipul', 'last_name':'Shah', 'age':24, 'status':'single'}
print(person)

print(person['status'])


# dict() constructor
tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(tel)

# dict comprehension
squares_dict = { f'Square of {x}' : x**2 for x in range(1,16)}
print(squares_dict)

# looping through dict
for k, v in person.items():
    print(k,v)