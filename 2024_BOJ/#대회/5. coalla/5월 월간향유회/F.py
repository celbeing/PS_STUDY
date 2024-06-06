import sys
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(1,0)]
R,C,T = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(R)]

def spread():
    next = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if A[x][y] == -1: continue
            k = A[x][y] // 5
            for i in range(4):
                dx = x+d[i][0]
                dy = y+d[i][1]
                if 0<=dx<R and 0<=dy<C:
                    next[dx][dy] += k
                    next[x][y] -= k
    for x in range(R):
        for y in range(C):
            A[x][y] += next[x][y]
    return

def air(x,y):
    while x > 0