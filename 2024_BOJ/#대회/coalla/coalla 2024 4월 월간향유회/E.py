# 23757: 아이들과 선물 상자
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N,M = map(int,input().split())
gift = []
c = list(map(int,input().split()))
for k in c: heappush(gift,-k)
w = list(map(int,input().split()))
result = True
for c in w:
    if c > -gift[0]:
        result = False
        break
    else:
        heappush(gift,heappop(gift)+c)
if result:
    print(1)
else:
    print(0)