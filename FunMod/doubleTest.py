import time
import numpy as np

tic = time.time()
a = np.random.rand(1000000)
b = np.random.rand(1000000)


# Vectorized version
c = np.dot(a, b)
toc = time.time()

print('c {0}'.format(c))
print('Performed within {0}'.format((toc - tic) * 1000))
print()

# Loop version
tic2 = time.time()
d = 0
for i in range(1000000):
    d += a[i] * b[i]
toc2 = time.time()

print('d {0}'.format(d))
print('Performed within {0}'.format((toc2 - tic2) * 1000))
