studentid = int(input("Enter student ID"))
name = input("Enter student name")
marks = float(input("Enter student marks"))
m1,m2,m3 = [float(x) for x in input("Enter three numbers separated by space").split()]
avg = (m1+m2+m3)/3

print("Student ID is %d , student name is %s and he scored %.2f marks in the exam"%(studentid, name, marks))
print("Average of the marks of the three subjects is %.2f"%(avg))