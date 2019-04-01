import re
str = "Hello Im Ankush Ankush Ankush"
result = re.search(r'A\w\w\w\w\w',str)
print(result.group())

'''It will takes all the charaters after the given string from 1 to all'''
result = re.findall(r'A\w+',str)
print(result)

'''It will takes all the characters from the given string from 0 to all'''
result = re.findall(r'A\w*',str)
print(result)

'''It will only take 0 and 1 character from the given string'''
result = re.findall(r'A\w?',str)
print(result)

'''The curly braces gives the characters of the number that is mentioned in the braces'''
result = re.findall(r'A\w{2}',str)
print(result)

'''This type takes the range in the curly braces followed by the first number is the minimum characters and 
the last number is the maximum characters'''
result = re.findall(r'A\w{2,5}',str)
print(result)

'''By Ankush Chavan'''