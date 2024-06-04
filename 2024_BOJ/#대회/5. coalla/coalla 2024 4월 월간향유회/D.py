# 14235: 크리스마스 선물
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
gift = []
for _ in range(n):
    v = list(map(int,input().split()))
    if v[0] == 0:
        if gift:
            print(-heappop(gift))
        else:
            print(-1)
    for i in range(1,v[0]+1):
        heappush(gift,-v[i])