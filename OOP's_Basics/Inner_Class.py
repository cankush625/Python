class car :
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    class engine :
        def __init__(self, number):
            self.number = number

        def display(self):
            print("Your Car is Ready!")

c1 = car("Lamborghini", 2016)
e1 = car.engine('LB2489u66')

e1.display()