import json

fruits = ["apple","banana"]

person = {"fname":"Vipul", "lname":"Shah", "fruits":fruits}

str = json.dumps(person)
print(str)