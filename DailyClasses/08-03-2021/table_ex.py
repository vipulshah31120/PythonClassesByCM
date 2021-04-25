def Table(x, i, l) :
	if i>l:			# it's i>L
		return
	print(x,"x",i,"=",x*i)
	i += 1
	Table(x, i, l)


Table(4, 1, 20) 