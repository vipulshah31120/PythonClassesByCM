def overflow(n) :
	print(n)
	n += 1
	overflow(n)


overflow(1)