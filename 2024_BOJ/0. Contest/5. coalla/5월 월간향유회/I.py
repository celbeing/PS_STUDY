import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]

def check(g,r):
    check = [[0]*M for _ in range(N)]
    green = deque(g)
    red = deque(r)

    flower = 0
    while green and red:
        while green:
            x,y = green.popleft()
            check[x][y] = 3
            for i in range(4):
                dx = x+d[i][0]
                dy = y+d[i][1]
                if 0 <= dx < N and 0 <= dy < M and ground[dx][dy] > 0:
                    if check[dx][dy] == 0: check[dx][dy] = 1
        while red:
            x,y = red.popleft()
            check[x][y] = 3
            for i in range(4):
                dx = x+d[i][0]
                dy = y+d[i][1]
                if 0 <= dx < N and 0 <= dy < M and ground[dx][dy] > 0:
                    if check[dx][dy] == 0: check[dx][dy] = 2
                    elif check[dx][dy] == 1:
                        flower += 1
                        check[dx][dy] = 3
        for i in range(N):
            for j in range(M):
                if check[i][j] == 1:
                    green.append((i,j))
                elif check[i][j] == 2:
                    red.append((i,j))
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