class Lamborghini :
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

class Gallardo(Lamborghini) :
    def __init__(self, cruisecontrolenabled, brand, model, year):
        Lamborghini.__init__(self, brand, model, year)
        self.cruisecontrolenabled = cruisecontrolenabled

    def display(self):
        print(self.cruisecontrolenabled)

class Aventador(Lamborghini):
    def __init__(self, parkingassistenabled, brand, model, year):
        Lamborghini.__init__(self, brand, model, year)
        self.parkingassistenabled = parkingassistenabled

    def display(self):
        print(self.parkingassistenabled)

G = Gallardo(True, "Lamborghini", "Gallardo", 2016)
print(G.cruisecontrolenabled)
print(G.brand)
print(G.model)
print(G.year)

G.start()
G.stop()
G.display()

A = Aventador(True, "Lamborghini", "Aventador", 2018)
print(A.parkingassistenabled)
print(A.brand)
print(A.model)
print(A.year)

A.start()
A.stop()
A.display()

'''By Ankush Chavan'''