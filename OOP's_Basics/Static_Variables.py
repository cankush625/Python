class student :
    '''It's a Static Variable whose value remains same throughout the class'''
    major = "CSE"

    def __init__(self, rollno, name):
        self.rollno = rollno
        self.name = name

s1 = student(1, "A")
s2 = student(2, "B")

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)

print(student.major)

'''By Ankush Chavan'''