import random
import time

ranInt = random.randint(0, 10)
# print(ranInt)

time.sleep(ranInt)
start_time = time.time()
input('Type as quick as you can')
end_time = time.time()

print('='*40)
print('Start time at: ', time.strftime("%X", time.localtime(start_time)))
print('Your pressed time at: ', time.strftime("%X", time.localtime(end_time)))
print('Your reaction: ', end_time - start_time)
