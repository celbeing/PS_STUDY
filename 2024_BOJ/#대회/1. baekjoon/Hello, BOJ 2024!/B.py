#B: 2024는 무엇이 특별할까?
import sys
from math import log2

input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    if log2(N)<K:
        print(0)
    else:
        k = 2**K
        N+=k
        k*=2
        print(N//k)