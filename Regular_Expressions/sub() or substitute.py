import re
str = "Hello Im Ankush"
result = re.search(r'A\w\w\w\w\w',str)
print(result.group())

result1 = re.sub(r'Hello', 'Good Morning', str)
print(result1)

'''By Ankush Chavan'''