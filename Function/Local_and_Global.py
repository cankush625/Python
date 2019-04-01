a = 123

def display() :
    a = 678
    print(a)
    print(globals()['a'])

print(a)
display()