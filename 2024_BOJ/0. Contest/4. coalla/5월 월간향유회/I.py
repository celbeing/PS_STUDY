import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]

def check(g,r):
    check = [[0]*M for _ in range(N)]
    green = deque(g)
    red = deque(r)
    for x,y in green:
        check[x][y] = -2
    for x,y in red:
        check[x][y] = -2

    flower = 0
    time = 1
    while green and red:
        ng = len(green)
        nr = len(red)
        for k in range(ng):
            x,y = green.popleft()
            if check[x][y] == -1: continue
            for i in range(4):
                dx = x+d[i][0]
                dy = y+d[i][1]
                if 0 <= dx < N and 0 <= dy < M and ground[dx][dy] > 0:
                    if check[dx][dy] == 0:
                        check[dx][dy] = time
                        green.append((dx,dy))
        for k in range(nr):
            x,y = red.popleft()
            for i in range(4):
                dx = x+d[i][0]
                dy = y+d[i][1]
                if 0 <= dx < N and 0 <= dy < M and ground[dx][dy] > 0:
                    if check[dx][dy] == 0:
                        check[dx][dy] = time+1
                        red.append((dx,dy))
                    elif check[dx][dy] == time:
                        flower += 1
                        check[dx][dy] = -1
        time += 2
    return flower

N,M,G,R = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
drops = []
for i in range(N):
    for j in range(M):
        if ground[i][j] == 2:
            drops.append((i,j))

flower = 0
comb = combinations(drops,G+R)
for gnr in comb:
    t = combinations(gnr, G)
    for p in t:
        g = []
        r = []
        for k in gnr:
            if k in p: g.append(k)
            else: r.append(k)
        flower = max(flower,check(g,r))
print(flower)