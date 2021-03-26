cars = ['ferarri', 'mazerati', 'lambo', 'toyota']
print(sorted(cars))

nums = [2,2,3,43,45,56,76,98,6,54,34,23,4,56]
print(sorted(nums))
print(sorted(nums, reverse=True))

print(sorted(set(nums)))


s1 = {1 : 'D', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E'}	#
print(sorted(s1))


string = "The value of the key parameter should be a function. "
print(sorted(string.split(), key=str.lower))

