#B: 실 전화기
from math import gcd
N,K = map(int,input().split())

g = gcd(N,K)
gN = N//g
gK = K//g
if gN//2 < gK:
    gK = gN-gK
print((gK-1)*gN)