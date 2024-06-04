# 19640: 화장실의 규칙
import sys
from collections import deque
from heapq import heappush,heappop
input = sys.stdin.readline
N,M,K = map(int,input().split())
line = [deque() for _ in range(M)]
front = []
count = 0
m,k = K%M,N//M
for i in range(N):
    d,h = map(int,input().split())
    line[i%M].append((-d,-h,i%M,i))
for i in range(M):
    line[i].append((1,1,-int(1e9),-1))
    heappush(front,line[i].popleft())

count = 0
while True:
    D,H,L,T = heappop(front)
    heappush(front,line[L].popleft())
    if T == K: break
    else: count += 1
print(count)