try:
    print("dusuds")
    raise Exception("Hum ek kudh Exception hai...")
except Exception as e:
	print(e) 
else:
	print("Bye")
finally:
	print("Done")


try :
	print(x)
except :
	print("x is Not Defined")



try :
	print(x)
except NameError:
	print("x is not deined.")
except :
	print("Something else went wrong.")


try :
	print("Hello")
except :
	print("Something is Wrong.")
else :
	print("Nothing went wrong.")



#	try :
#		f = open("readme.md")
#		f.write("Hello")
#	except :
#		print("Something went wrong while writing a file.")
#	finally :
#		f.close()


x = 2 #use -2

if x<0 :
	raise Exception("Unmatched Number")


x = "Arreeyy"

if not type(x) is int :
	raise TypeError("Only integers are allowed.")	




x = 54
	
if not type(x) is str :
	raise TypeError("Only Strings are allowed.")


