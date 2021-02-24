class Vehicle :
	def __init__(self, nTyre, loadCap) :
		self.nTyre = nTyre
		self.loadCap = loadCap

	def show(self):
		print(" No. of tyres :", self.nTyre)	
		print("Load Capacity : ", self.loadCap)


v1 = Vehicle(4, 77)

v1.show()  # correct way
print(v1.show())  # incorrect way because will return NONE


class Car(Vehicle):
	def __init__(self, nTyre, loadCap, brand) :  # brand is made under class of car, if we made method of brand in vehicle then there is no use of inheritence 
		Vehicle.__init__(self, nTyre, loadCap)   # brand is the property of car only, tyre n loadcap are properties of vehicle and cuz car is a(inheritance) vehicle so, it also has loadcap and tyre property due to inheritance
		self.brand = brand					     # inheritance -> is-a relationship

	def showBrand(self):
		print(self.brand)


c = Car(12, 1000, "Maruti")
c.show()
c.showBrand()


class Bike(Vehicle):
	def __init__(self, nTyre, loadcap, type):
		super().__init__(nTyre, loadcap)  # we can also use super() function for parent reference and we can access parents properties with it
		self.type = type				  # and we don't need to pass self while calling it like Vehcle.__init__(self, nTyre, loadCap)


b = Bike(2, 100, "Sports")
b.show()


