import re
str = "Hello 1-2-1017 Im 01-02-2017Ankush 12-2-2015"
result = re.search(r'A\w\w\w\w\w',str)
print(result.group())

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(result)

'''By Ankush Chavan'''