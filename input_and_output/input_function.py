print("Please enter your name : ")
name=input()
print(name)

age=input("Enter your age : ")
print(age)
print(type(age))

'''int is used before input to convert age variable from string to the integer else it is of the type string'''
'''Here age is type cascaded to int'''
age=int(input("Enter your age : "))
print(age)
print(type(age))