try:
    print("dusuds")
    raise Exception("Hum ek kudh Exception hai...")
except Exception as e:
	print(e) 
else:
	print("Bye")
finally:
	print("Done")
