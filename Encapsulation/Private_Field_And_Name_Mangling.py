class student :
    def __init__(self):
        self.__id = 12345
        self.__name = "Ankush"

    def display(self):
        print(self.__id)
        print(self.__name)

s1 = student()
print(s1._student__id)
print(s1._student__name)

s1.display()

'''By Ankush Chavan'''