# H: 저체온증
import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
N,M,K = map(int,input().split())
p = [list(input()) for _ in range(N)]
check = [[0] * M for _ in range(N)]

bfs = deque()
for i in range(N*M):
    r = i//M
    c = i%M
    if p[r][c] == '.':
        bfs.append((r,c))
    while bfs:
        nr,nc = bfs.popleft()
        nearby = 0
        blanks = []
        for i in range(4):
            dr = nr+d[i][0]
            dc = nc+d[i][1]
            if 0<=dr<N and 0<=dc<M:
                if p[dr][dc] == '.':
                    blanks.append((dr,dc))
                else:
                    nearby+=1
            if nearby>=2:
                p[nr][nc] = 'O'
                while blanks:
                    bfs.append(blanks.pop())

recovered = 0
bfs.clear()
for i in range(N*M):
    r = i//M
    c = i%M
    if p[r][c] == 'O' and check[r][c] == 0:
        h,w = r,c
        while h < N and p[h][c] == 'O': h+=1
        while w < M and p[r][w] == 'O': w+=1
        for j in range(r,h):
            for k in range(c,w):
                check[j][k] = 1
        if h-r > K and w-c > K:
            recovered+=(h-r)*(w-c)
print(recovered)