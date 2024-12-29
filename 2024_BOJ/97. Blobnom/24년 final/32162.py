# 32162: n, 3n, 5n
import sys
from heapq import heappush, heappop
from math import gcd
input = sys.stdin.readline
def solution():
    a = [0]
    k = []
    for i in range(1, 167219):
        if gcd(15, i) == 1:
            heappush(k, i)
    while k and len(a) < 100001:
        a.append(heappop(k))
        if a[-1] % 3:
            heappush(k, a[-1] * 125)
        if a[-1] % 5:
            heappush(k, a[-1] * 27)
        heappush(k, a[-1] * 15)
    for _ in range(int(input())):
        print(a[int(input())])
solution()