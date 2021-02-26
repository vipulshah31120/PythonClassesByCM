import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%d"))  # Day of month 01-31
print(x.strftime("%A"))	 # Weekday, full version
print(x.strftime("%B"))	 # Month name, full version
print(x.strftime("%p"))
print(x.strftime("%Z"))

from datetime import timedelta
delta = timedelta(			   # 1st method
		days = 50,
		seconds = 27,
		microseconds = 10,
		milliseconds = 20000,
		minutes = 5,
		hours = 8,
		weeks = 4
	)

print(delta)

print(datetime.timedelta(days = 64, seconds = 49387, microseconds = 10))  #2nd method
