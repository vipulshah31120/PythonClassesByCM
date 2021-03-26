f = open("Python Classes by me", "r")
print(f.read())
#print(f.read()) 	#Return the 5 first characters of the file

#print(f.readline()) 	#You can return one line by using the readline() method

f = open("Python Classes by me", "a")
f.write("\nNow the file has more content!")
f.close()