'''The abstracted function must be used in all of the classes else error will be occured'''

from abc import abstractmethod, ABC
class Lamborghini(ABC) :
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Starting the car")

    def stop(self):
        print("Stopping the car")

    @abstractmethod
    def drive(self):
        pass

class Gallardo(Lamborghini) :
    def __init__(self, cruisecontrolenabled, brand, model, year):
        super().__init__(brand, model, year)
        self.cruisecontrolenabled = cruisecontrolenabled

    def display(self):
        print(self.cruisecontrolenabled)

    def start(self):
        super().start()
        print("Button Start")

    def drive(self):
        print("Gallardo is being driven")

class Aventador(Lamborghini):
    def __init__(self, parkingassistenabled, brand, model, year):
        super().__init__(brand, model, year)
        self.parkingassistenabled = parkingassistenabled

    def display(self):
        print(self.parkingassistenabled)

    def drive(self):
        print("Aventador is being driven")

G = Gallardo(True, "Lamborghini", "Gallardo", 2016)
print(G.cruisecontrolenabled)
print(G.brand)
print(G.model)
print(G.year)

G.start()
G.stop()
G.display()
G.start()
G.drive()

A = Aventador(True, "Lamborghini", "Aventador", 2018)
print(A.parkingassistenabled)
print(A.brand)
print(A.model)
print(A.year)

A.start()
A.stop()
A.display()
A.drive()

'''By Ankush Chavan'''