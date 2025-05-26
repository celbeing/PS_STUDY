from math import ceil, floor
res = 0
a, b = map(int, input().split())
a = ceil(a**0.5)
b = floor((b**0.5) + 1)
b = int(b)
for i in range(a, b):
    res += i ** 2
print(res)