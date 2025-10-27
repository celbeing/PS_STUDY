# 22718: Divisor Function
import sys
input = sys.stdin.readline

high = 0
k = 1
while 1:
    if k % 100000 == 0: print(f'now k is {k}...')
    sig = 0
    for f in range(1, int(k ** 0.5) + 1):
        if f * f == k:
            sig += f
        elif k % f == 0:
            sig += f + k // f
    res = sig / k
    if res > high:
        high = res
        print(f'from {k}, result is updated to {res}')
    k += 1