import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N,K = map(int,input().split())
bfs = [(0,0,0)]
d = [(1,0),(0,1),(-1,0),(0,-1)]
visit = {}

item = [tuple(map(int,input().split())) for _ in range(N)]

E = tuple(map(int,input().split()))
while bfs:
    sta,x,y = heappop(bfs)
    if (x,y) == E:
        break
    for i in range(4):
        dx = x+d[i][0]
        dy = y+d[i][1]
        if (dx,dy) in visit:
            continue
        else:
            visit[(dx,dy)] = sta+1
            heappush(bfs,(sta+1,dx,dy))
    for a,b in item:
        dx = x+a
        dy = y+b
        if (dx,dy) in visit:
            continue
        else:
            visit[(dx,dy)] = sta+2
            heappush(bfs,(sta+2,dx,dy))
if E in visit:
    print(visit(E))
else:
    print(-1)