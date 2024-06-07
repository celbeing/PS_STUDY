#13172: ∑
import sys
from math import gcd
input = sys.stdin.readline
M = int(input())
mod = 1000000007
result = 0

def comp(a,b,c):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res *= a
            res %= c
            b -= 1
        a *= a
        a %= c
        b //= 2
    return res

for _ in range(M):
    n,s = map(int,input().split())
    g = gcd(n,s)
    n //= g
    s //= g
    result += s*comp(n,mod-2,mod)%mod
    result %= mod

print(result)