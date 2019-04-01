import re
str = "Hello Im Ankush"
result = re.search(r'A\w\w\w\w\w',str)
print(result.group())

'''The '^' Character only searches the first word of the string'''
result1 = re.search(r'^H\w*',str)
print(result1.group())

'''By Ankush Chavan'''