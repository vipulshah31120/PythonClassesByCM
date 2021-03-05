import json

fruits = ["apple","banana"]

person = {"fname":"Vipul", "lname":"Shah", "fruits":fruits}

str = json.dumps(person)
print(str)



cars = ["BMW", "Pagani", "Konigsegg", "LaFerrari"]

Myself = ["I have these cars :",cars]

Mycars = json.dumps(Myself)
print(Mycars)





x = '{"name":"Niklaus", "age":"Immortal", "City":"New Orleans"}'

y = json.loads(x)

print(y["City"])

a = {
		"Name": "Marcel",
		"Age": "800 Years",
		"Married": True,
		"Divorced": False,
		"Friends" : ("Vincent", "Camille"),
		"Enemy" : "Niklaus",
		"Bikes" : [
				{"Model":"Ford", "color":"Black"},
				{"Model": "Chevrolet", "color":"Blue"}
		]	   	
	}

print(json.dumps(a))
print(json.dumps(a, indent = 4, separators=(". ", " = ")))
