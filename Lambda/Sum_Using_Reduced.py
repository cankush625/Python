from functools import reduce

lst = [10, 20, 30, 40]

f = reduce(lambda x,y : x+y, lst)

print(f)

'''By Ankush Chavan'''