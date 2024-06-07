import sys
from math import gcd
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    g = [[]*n for _ in range(2)]
    for i in range(n-2):
        g[i][0] = gcd(a[i],a[i+1])
        g[i][1] = gcd(a[i],a[i+2])
    g[-2][0] = gcd(a[-2],a[-1])
