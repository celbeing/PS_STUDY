import sys
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
R,C,T = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(R)]

def spread():
    next = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] == -1: continue
            k = A[x][y] // 5
            if k == 0: continue
            for i in range(4):
                dx = x+d[i][0]
                dy = y+d[i][1]
                if 0<=dx<R and 0<=dy<C and A[dx][dy] > -1:
                    next[dx][dy] += k
                    next[x][y] -= k
    for x in range(R):
        for y in range(C):
            A[x][y] += next[x][y]
    return

def air(x):
    r = x-1
    c = 0
    while r > 0:
        A[r][c] = A[r-1][c]
        r -= 1
    while c < C-1:
        A[r][c] = A[r][c+1]
        c += 1
    while r < x:
        A[r][c] = A[r+1][c]
        r += 1
    while c > 1:
        A[r][c] = A[r][c-1]
        c -= 1
    A[r][1] = 0
    c = 0
    r += 2
    while r < R-1:
        A[r][c] = A[r+1][c]
        r += 1
    while c < C-1:
        A[r][c] = A[r][c+1]
        c += 1
    while r > x+1:
        A[r][c] = A[r-1][c]
        r -= 1
    while c > 1:
        A[r][c] = A[r][c-1]
        c -= 1
    A[x+1][1] = 0

airR = 0
for i in range(2,R-2):
    if A[i][0] == -1:
        airR = i
        break

for i in range(T):
    spread()
    air(airR)

count = 0
for x in range(R):
    for y in range(C):
        if A[x][y] > 0: count += A[x][y]
print(count)