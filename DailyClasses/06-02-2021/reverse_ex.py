list = [1,2,3,5,76,87,78,85,645,43,32,1,4,665,9]
print(list)
for x in reversed(list) :
    print(x, end=', ')  #'end=' parameter is ‘\n’, i.e. the new line character. 

print(list.reverse())   #it returns None.



#In this particular example, the slice statement [::-1] means start at the end of the string and end 
#at position 0, move with the step -1, negative one, which means one step backwards.

txt = "Vipul Shah"[::-1]
print(txt)



def r1(n) :
	return n[::-1]

txt1 = r1("Hello, My name is Mr. Sherlock Holmes.")
txt2 = r1(".semloH kcolrehS .rM si eman yM ,olleH")
print(txt1)
print(txt2)



