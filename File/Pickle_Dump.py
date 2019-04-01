import pickle, Student

f = open("student.dat", "wb")
s = Student.student(12345, "Ankush", 99)

pickle.dump(s,f)
f.close()

'''By Ankush Chavan'''