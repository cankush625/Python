dict1={1:"C", 2:"C++", 3:"Python", 4:"Ruby"}
print(dict1)
print(type(dict1))

k=dict1.keys()
for i in k:
    print(i)

print()

j=dict1.values()
for i in j:
    print(i)

print()
print(dict1[3])

print()
del dict1[4]
print(dict1)