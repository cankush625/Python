import re
str = "Hello Im Ankush"
result = re.search(r'A\w\w\w\w\w',str)
print(result.group())

result = re.findall(r'A\w\w\w\w\w',str)
print(result)

result = re.findall(r'a\w\w\w\w\w',str)
print(result)

'''Match matches only the first matching string and if another matching word is there in the string then
it ignores the matching words there after. It only prints the first matching word'''
result = re.match(r'A\w\w\w\w\w',str)
print(result)

result = re.match(r'a\w\w\w\w\w',str)
print(result)

result = re.match(r'H\w\w\w',str)
print(result)

result = re.match(r'H\w\w\w\w',str)
print(result.group())

'''By Ankush Chavan'''