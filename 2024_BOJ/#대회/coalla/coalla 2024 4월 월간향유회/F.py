# 19640: 화장실의 규칙
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
line = [deque() for _ in range(M)]
count = 0
m,k = K%M,N//M
for i in range(N):
    line[i%M].append(tuple(map(int,input().split())))
