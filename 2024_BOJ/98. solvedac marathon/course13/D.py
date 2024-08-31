#16926: 배열 돌리기 1
import sys
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
N,M,R = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(N)]
res = [[0]*M for _ in range(N)]
for l in range(min(N,M)//2):
    x,y,h,w = l,l,N-l*2,M-l*2
    dr = 0
    rx,ry = x,y
    for r in range(R):
        rx += d[dr][0]
        ry += d[dr][1]
        if not(0<=rx-l<h and 0<=ry-l<w):
            rx -= d[dr][0]
            ry -= d[dr][1]
            dr = (dr+1)%4
            rx += d[dr][0]
            ry += d[dr][1]
    for i in range(h-1):
        res[rx][ry] = A[x][y]
        x += 1
        rx += d[dr][0]
        ry += d[dr][1]
        if not(0<=rx-l<h and 0<=ry-l<w):
            rx -= d[dr][0]
            ry -= d[dr][1]
            dr = (dr + 1) % 4
            rx += d[dr][0]
            ry += d[dr][1]
    for i in range(w-1):
        res[rx][ry] = A[x][y]
        y += 1
        rx += d[dr][0]
        ry += d[dr][1]
        if not(0<=rx-l<h and 0<=ry-l<w):
            rx -= d[dr][0]
            ry -= d[dr][1]
            dr = (dr + 1) % 4
            rx += d[dr][0]
            ry += d[dr][1]
    for i in range(h-1):
        res[rx][ry] = A[x][y]
        x -= 1
        rx += d[dr][0]
        ry += d[dr][1]
        if not(0<=rx-l<h and 0<=ry-l<w):
            rx -= d[dr][0]
            ry -= d[dr][1]
            dr = (dr + 1) % 4
            rx += d[dr][0]
            ry += d[dr][1]
    for i in range(w-1):
        res[rx][ry] = A[x][y]
        y -= 1
        rx += d[dr][0]
        ry += d[dr][1]
        if not(0<=rx-l<h and 0<=ry-l<w):
            rx -= d[dr][0]
            ry -= d[dr][1]
            dr = (dr + 1) % 4
            rx += d[dr][0]
            ry += d[dr][1]
for i in range(N):
    print(*res[i])