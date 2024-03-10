#1086: 박성원
import sys
from math import gcd, factorial
input = sys.stdin.readline

N = int(input())
n = [int(input()) for _ in range(N)]
K = int(input())
remain = [[-1]*(1<<N) for _ in range(K+1)]
for i in range(N):
    remain[i][0] %= K
    for j in range(1,N):
        remain[i][j] = (remain[i][j-1]*10)%K