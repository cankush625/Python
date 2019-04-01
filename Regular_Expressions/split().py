import re
str = "Hello 1 Im 234 Ankush"
result = re.search(r'A\w\w\w\w\w',str)
print(result.group())


'''By using split we can determine by using which splitter it should split the string. That here we used the 
numbers in between the string or a complete statement and split tge string from where the numbers are in the
sentence and print all the  parts of the statement in the form of the list'''
result1 = re.split(r'\d+',str)
print(result1)

'''By Ankush Chavan'''