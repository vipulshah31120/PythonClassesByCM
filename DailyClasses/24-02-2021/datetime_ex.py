# we have a datetime module in python for datetime related work
# we need to import datetime module before using it

import datetime
import time

t = datetime.datetime.now()

d = datetime.date.today()

print(d)
print(t)
print(t.year)
print(t.strftime("%D"))


currentTime = time.time()  # from 1st jan, 1970 till now -> seconds
print(currentTime)