print("To find largest number among provided numbers ")
print("The largest number is ",max(24,67,45))

print()
print()
print("To find smallest number from provided numbers")
print("The smallest number is ",min(24,67,45))

print()
print()
print("To find largest number from the three numbers given by user")
print("Enter three numbers")
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number "))
if(num1>num2) and (num1>num3):
    largest=num1
    elif (num2>num1) and (num2>num3):
        largest=num2
else :
largest=num3
print("The largest number is",largest)