class Lamborghini :
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

class Gallardo(Lamborghini) :
    def __init__(self, cruisecontrolenabled, brand, model, year):
        Lamborghini.__init__(self, brand, model, year)
        self.cruisecontrolenabled = cruisecontrolenabled

class Aventador(Lamborghini):
    def __init__(self, parkingassistenabled, brand, model, year):
        Lamborghini.__init__(self, brand, model, year)
        self.parkingassistenabled = parkingassistenabled

G = Gallardo(True, "Lamborghini", "Gallardo", 2016)
print(G.cruisecontrolenabled)
print(G.brand)
print(G.model)
print(G.year)

A = Aventador(True, "Lamborghini", "Aventador", 2018)
print(A.parkingassistenabled)
print(A.brand)
print(A.model)
print(A.year)

'''By Ankush Chavan'''