try :
    a, b = [int(x) for x in input("Enter two numbers : ").split()]
    c =a/b
    print(c)
except ZeroDivisionError :
    print("Division by zero is not allowed")
    print("Please enter non-zero number")

print("Here is the code after the exception")