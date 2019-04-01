print("Press Enter to Enter two number in between which you want to find odd numbers")
a = int(input("Enter one number"))
b = int(input("Enter another number"))
x = a
while(x<b):
    if x%2!=0:
        print("%d is a odd number between %d and %d"%(x, a, b))
    x+=1