import time
from time import time as now

print(time.gmtime())
print('='*40)
print(time.localtime())
print('='*40)
print(time.time())
print(time.strftime('%X', time.localtime(now())))
print()


print('*'*80)
curr_time = time.localtime()
print(curr_time)
print('YEAR: ', curr_time[0])
print('MONTH: ', curr_time[1])
print('DAY: ', curr_time[2])


