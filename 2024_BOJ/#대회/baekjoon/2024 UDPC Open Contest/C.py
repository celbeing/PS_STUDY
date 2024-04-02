#31714: 지정좌석 배치하기 1
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
N,M,D = map(int,input().split())
flag = True
h = [[] for _ in range(N)]
for i in range(N):
    seat = list(map(int, input().split()))
    for k in seat:
        if k > D: heappush(h[i],D-k)
        else: heappush(h[i],0)

for _ in range(M):
    for i in range(N-1):
        if h[i][0]<0:
            if h[i][0] < h[i+1][0]-D:
                flag = False
                break
        heappop(h[i])
    if ~flag: break
if flag: print("YES")
else: print("NO")