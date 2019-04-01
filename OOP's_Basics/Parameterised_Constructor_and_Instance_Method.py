class course :
    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings

    def average(self):
        numberofratings = len(self.ratings)
        average = sum(self.ratings)/numberofratings
        print("Average rating for ",self.name,"is ",average)

p1 = course(name="Java Course", ratings=[1,2,3,4,5])

print(p1.name)
print(p1.ratings)
p1.average()

p2 = course("Java Web Services",[6,7,8,9,10])

print(p2.name)
print(p2.ratings)
p2.average()