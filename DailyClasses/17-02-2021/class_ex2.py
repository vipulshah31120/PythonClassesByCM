class Student:
	def __init__(self, name, age, subjects, stream, sports) :
		self.name = name
		self.age = age
		self.subjects = subjects
		self.stream = stream
		self.sports = sports

	def myself(self) :
		essay = f''' 
				My name is {self.name}. My age is {self.age}. I study these {len(self.subjects)} subjects: {self.subjects}. 

				Also, i am involved in sports which are {self.sports}. My stream is {self.stream}.
			'''
		return essay	

sports = ['Swimming', 'Badminton', 'Golf', 'Basketball']

subjects = {"Maths" : 55, "Science" : 75, "English" : 89 }

s1 = Student("Shubham", 22, subjects, "IT", sports)

print(s1.myself())

