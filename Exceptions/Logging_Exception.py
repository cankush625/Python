import logging

logging.basicConfig(filename="my_log.log", level=logging.DEBUG)
try :
    f = open("myfile", "w")
    a, b = [int(x) for x in input("Enter two numbers : ").split()]
    logging.info("Division is in progress")
    c =a/b
    f.write("Writing %d into the file " %c)
except ZeroDivisionError :
    print("Division by zero is not allowed")
    print("Please enter non-zero number")
    logging.error("Division by zero !!!")
else :
    print("You have enetred a non-zero number")
finally :
    f.close()
    print("File Closed")

print("Here is the code after the exception")

'''By Ankush Chavan'''