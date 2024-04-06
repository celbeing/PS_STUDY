#A: 매우 어려운 문제
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
if N>=M: print(0)
else:
    k = 1
    for i in range(2, N+1):
        k*=i
        k%=M
    print(k)