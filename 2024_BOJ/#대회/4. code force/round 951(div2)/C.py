import sys
from math import gcd
input = sys.stdin.readline
t = int(input())

def lcm(a,b):
    return a*b//gcd(a,b)

for _ in range(t):
    n = int(input())
    k = list(map(int,input().split()))
    limit = k[0]
    for i in range(1,n):
        limit = lcm(limit,k[i])
    p = [0]*n
    for i in range(n):
        p[i] = limit // k[i]
    total = sum(p)
    while total > 0:
        flag = True
        for i in range(n):
            get = total//k[i]-p[i] + 1
            if get > 0:
                flag = False
                p[i] += get
                total += get
                if total > limit:
                    total = -1
                    break
        if flag: break
    if total > 0: print(*p)
    else: print(-1)