lst=[10, 20, 30, 40, 50]
print(type(lst))

b=bytes(lst)
print(type(b))

b1=bytearray(lst)
print(type(b1))
b1[4]=60
print(b1)