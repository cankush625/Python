maths = int(input("Enter your marks of maths"))
physics = int(input("Enter your marks of physics"))
chemistry = int(input("Enter your marks of the chemistry"))
avg = (maths+physics+chemistry)/3
if maths>=35 and physics>=35 and chemistry>=35 :
    print("You are passed in maths, physics and chemistry")
    print("Your average of the subjects is %d"%avg)
    if avg<=59 :
        print("You are passed with C grade")
    elif avg<=69 :
        print("You are passed with B grade")
    elif avg>=70 :
        print("You are passed with A grade")
elif maths<35 :
    print("You are failed in maths")
    if chemistry < 35:
        print("You are failed in chemistry")
    elif physics < 35:
        print("You are failed in physics")
elif physics<35 :
    print("You are failed in physics")
    if chemistry < 35:
        print("You are failed in chemistry")
    elif maths < 35:
        print("You are failed in maths")
elif chemistry<35 :
    print("You are failed in chemistry")
    if maths < 35:
        print("You are failed in maths")
    elif physics < 35:
        print("You are failed in physics")