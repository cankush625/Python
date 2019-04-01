try :
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter two numbers : ").split()]
    c =a/b
    f.write("Writing %d into the file " %c)
except ZeroDivisionError :
    print("Division by zero is not allowed")
    print("Please enter non-zero number")
else :
    print("You have enetred a non-zero number")
finally :
    f.close()
    print("File Closed")

print("Here is the code after the exception")

'''By Ankush Chavan'''