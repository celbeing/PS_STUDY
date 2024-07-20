import sys
from heapq import heappush,heappop
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
H,W,Y = map(int,input().split())
land = [list(map(int,input().split())) for _ in range(H)]
check = [[0]*W for _ in range(H)]
year = [H*W]*(Y+1)

hq = []
now = 0
for i in range(W):
    if not check[0][i]:
        heappush(hq,(land[0][i],0,i))
        check[0][i] = 1
    if not check[-1][i]:
        heappush(hq,(land[-1][i],H-1,i))
        check[-1][i] = 1
for i in range(1,H-1):
    if not check[i][0]:
        heappush(hq,(land[i][0],i,0))
        check[i][0] = 1
    if not check[i][-1]:
        heappush(hq,(land[i][-1],i,W-1))
        check[i][-1] = 1

count = 0
while hq and now <= Y:
    now = hq[0][0]
    while hq and hq[0][0] <= now:
        count += 1
        l,h,w = heappop(hq)
        for i in range(4):
            dh = h + d[i][0]
            dw = w + d[i][1]
            if 0<=dh<H and 0<=dw<W and not check[dh][dw]:
                check[dh][dw] = 1
                if land[dh][dw] > Y:
                    continue
                heappush(hq,(land[dh][dw],dh,dw))
    if hq:
        for i in range(now,min(hq[0][0],Y+1)):
            year[i] -= count
    else:
        for i in range(now,Y+1):
            year[i] -= count
for i in range(1,Y+1):
    print(year[i])