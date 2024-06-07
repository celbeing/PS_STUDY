#C: Y
import sys
from math import comb
input = sys.stdin.readline
n,m = map(int,input().split())
y = [0 for _ in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    y[u] += 1
    y[v] += 1
result = 0
for a in y:
    result += comb(a,3)
    result %= 1000000007
print(result)