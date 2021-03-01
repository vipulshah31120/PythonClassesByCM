class Laptop :
	def __init__(self, name, price) :
		self.name = name
		self.price = price

	def show(self) :
		print("Laptop Name: ", self.name)
		print("Laptop price: ", self.price)

l1 = Laptop("Lenovo", 45000)

l1.show()

class Laptop2(Laptop) :
	def __init__(self, name, price, color) :
		Laptop.__init__(self, name, price)
		self.color = color

	def showcolor(self) :
		print("Laptop Color: ", self.color)
		print("Laptop name: ", self.name)
		print("Laptop price: ", self.price)

l2 = Laptop2("HP", 35000, "Black")
l2.showcolor()

