import time, datetime
epocheseconds = time.time()
print(epocheseconds)

t = time.ctime(epocheseconds)
print(t)

dt = datetime.datetime.today()
print(dt)

'''The brackets{} are placeholders and the slashes '\' and colons ':' are used as separators between day,
month and year, etc'''
print("Todays date is : {}/{}/{}".format(dt.day, dt.month, dt.year))
print("Current time is : {}:{}:{}".format(dt.hour, dt.minute, dt.second))