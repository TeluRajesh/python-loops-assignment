import numpy as np

temp_celsius = np.array([22, 25, 28, 24, 26])

fa = temp_celsius * 1.8 + 32

print(temp_celsius)

print(fa)

print(f"avg : {fa.mean():.1f}")


arr = np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])
print(arr.shape)
print(arr.size)
print(arr.max())
print(arr.min())
print(arr.max() - arr.min())


import time
a = np.arange(1, 50001)
b = list(range(1, 50001))
start = time.time()
a.sum()
end = time.time()
time1 = end - start
print(end - start)

start2 = time.time()
np.sum(b)
end2 = time.time()
time2 = end2 - start2
print(end2 - start2)
print(time1/time2 * 100)