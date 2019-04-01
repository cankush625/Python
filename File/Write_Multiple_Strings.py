f = open("myfile.txt", "w")
print("Enter the text (Enter # when you are done) : \n")

s = ''
while s != '#' :
    s = input()
    f.write(s+("\n"))
f.close()

'''By Ankush Chavan'''