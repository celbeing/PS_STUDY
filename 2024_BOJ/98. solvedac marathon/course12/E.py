#20157: 화살을 쏘자!
import sys
from math import gcd
input = sys.stdin.readline
N = int(input())
high = 0
dir = dict()
for _ in range(N):
    x,y = map(int,input().split())
    k = gcd(x,y)
    x,y = x//k, y//k
    dir[(x,y)] = dir.get((x,y),0)+1
    if high < dir[(x,y)]: high = dir[(x,y)]
print(high)