lst=[x for x in input("Enter three numbers separated by space : ").split()]
print(lst)

'''We can also use separator comma in the split function to separate the elements by comma'''

lst1=[x for x in input("Enter three numbers separated by comma : ").split(',')]
print(lst1)
print(type(lst1))

'''We can simply make it of the type of int by simply typing int before x'''

lst2=[int(x) for x in input("Enter three numbers separated by comma : ").split(',')]
print(lst2)
print(type(lst2))

'''By Ankush Chavan'''