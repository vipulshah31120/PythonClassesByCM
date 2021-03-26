f = open("party_planning.txt", "a")
f.write('Party karenge....')
f.write('\nKya vichar hai aapka??')
f.write('\nVichar to badiya...pr krna kya hai')

f.close()

fRead = open("party_planning.txt", "r")

print(fRead.readline())
print(fRead.read(20))
print(fRead.readline())
fRead.close()

import os

if os.path.exists('party_planning.txt'):
	print('file exists')
	# os.remove('party_planning.txt')
else:
	print('no file exists')