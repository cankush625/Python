class programmer :
    def setname(self,name):
        self.name = name

    def getname(self):
        return self.name

    def setsalary(self,salary):
        self.salary = salary

    def getsalary(self):
        return self.salary

    def settechnology(self,technology):
        self.technology = technology

    def gettechnology(self):
        return self.technology

p1 = programmer()
p1.setname('Ankush')
p1.setsalary(2500000)
p1.settechnology(["Python", "C", "C++", "Java", "HTML"])

print(p1.getname())
print(p1.getsalary())
print(p1.gettechnology())