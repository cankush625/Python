from datetime import *
import time

starttime = time.perf_counter()

lstdates = []

d1 = date(2015, 9, 20)
d2 = date(2014, 11, 12)
d3 = date(2018, 11, 6)

lstdates.append(d1)
lstdates.append(d2)
lstdates.append(d3)

lstdates.sort()

time.sleep(3)

for i in lstdates :
    print(i)

endtime = time.perf_counter()

print("Executon time : ",endtime-starttime)

'''By Ankush Chavan'''