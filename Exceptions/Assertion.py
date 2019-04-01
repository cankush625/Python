try :
    num = int(input("Enter a even number : "))
    assert num%2 == 0, "You have entered odd number"
except AssertionError as obj :
    print(obj)
'''Or we can write simply as :
    except AssertionError :
        print("You have entered odd number")'''
print("Code after assertion")