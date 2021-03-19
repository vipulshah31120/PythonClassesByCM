price  = 55
txt = "The price of CNG is {} Rupees."
print(txt.format(price))

txt = "The price of CNG is {:.2f} Rupees."
print(txt.format(price))

color = "Black"
car = "G Wagon"
price = "2 CR"

t1 = "I want a {} of {} color which costs {}."
print(t1.format(car, color, price))

t1 = "I want a {0} of {2} color which costs {2}."
print(t1.format(car, color, price))


t1 = "I want a {car} of {color} color which costs {price}."
print(t1.format(car = "Mustang", color = "Red" , price = "5CR"))		# all 3 areguments should be written

