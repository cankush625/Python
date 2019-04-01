from datetime import *

d = date(2018, 11, 6)
t = time(16, 18)

dt = datetime.combine(d, t)
print(dt)