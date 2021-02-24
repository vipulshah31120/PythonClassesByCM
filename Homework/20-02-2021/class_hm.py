class Vehicle :
	def __init__(self, nTyres, loadCap) :
		self.nTyres = nTyres
		self.loadCap = loadCap

	def show(self) :
		print("No. of Tyres: ", self.nTyres)
		print("Load Capacity: ", self.loadCap)

v1 = Vehicle(5, "10 Ton" )
print(v1.nTyres)
print(v1.loadCap)

v1.show()


class Car(Vehicle) :
	def __init__(self, nTyres, loadCap, brand) :
		Vehicle.__init__(self, nTyres, loadCap)
		self.brand = brand

	def showbrand(self) :
		print("Car Brand : ", self.brand)

c1 = Car(6, "55 Ton", "Toyota")
#c1.show()
c1.showbrand()


class Bike(Vehicle) :
	def __init__(self, nTyres, loadCap, type) :
		super().__init__(nTyres, loadCap)
		self.type = type

	def showtype(self) :
		print("Type : ", self.type)

b1 = Bike(9, "25 Ton", "Sports")
b1.show()
b1.showtype()
