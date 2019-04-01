s={10, 20, 30, 40, 50, 10, 20}
#set does not allows duplicate or repeated elements
print(s)
print(type(s))

s.update([60, 70])
print(s)

s.remove(70)
print(s)

f=frozenset(s)
print(f)