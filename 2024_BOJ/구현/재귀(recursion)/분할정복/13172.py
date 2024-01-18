#13172: ∑
import sys
from math import gcd
input = sys.stdin.readline
M = int(input())
for _ in range(M):
    n,s = map(int,input().split())
    g = gcd(n,s)
    n //= g
    s //= g
    print(n,s)