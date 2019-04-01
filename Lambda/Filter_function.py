lst = [10, 20, 30, 45, 65, 79, 88]

f = list(filter(lambda x:x%2==0, lst))

print(f)

for i in f :
    print(i)