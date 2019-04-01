print()
print("Hello"*3)
'''\n is used to take a new line'''
print("Im \n Ankush")

a,b=10,20
print(a,b)
'''The sep is used to separate two elements using any separator that we have provided in the two single quiotes'''
print(a,b,sep=',')
'''This time the elements are get separated by the hash sign'''
print(a,b,sep='###')

name="Ankush"
marks=97.71

print("Name is ",name, ", marks are ",marks)
print("Name is %s and marks are %f"%(name, marks))
'''Here we used .2 in between % and f . This is used to print answer only upto two decimal points.
Simply replace the 2 by number for how many decimal places required to you in your answer'''
print("Name is %s and marks are %.2f"%(name, marks))

print("Name is {} and marks are {}".format(name, marks))

print("Name is {0} and marks are {1}".format(name, marks))

'''By Ankush Chavan'''