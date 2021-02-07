places = {'london' :11 , 'viana' :12 , 'denver' :13, 'prague' :14}
places['las vegas']=15
print(places)

del places['london']

places['sweden']=11     #it will be added in last
print(places)

print(list(places))
print(sorted(places))   #print letter wise

print('london' in places)
print('viana' in places)

# looping through dict
for k,v in places.items() :
    print(k,v)
    
for k,v in enumerate(places) :
    print(k,'-',v)