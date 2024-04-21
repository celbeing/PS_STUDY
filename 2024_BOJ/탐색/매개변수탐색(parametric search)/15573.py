#15573: 채굴
import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
N,M,K = map(int,input().split())
S = [list(map(int,input().split())) for _ in range(N)]

def bfs(field, h):
    ret = 0
    check = [[0]*M for _ in range(N)]
    dq = deque()
    for i in range(M):
        if field[0][i] <= h:
            dq.append((0,i))
            check[0][i] = 1
            ret += 1
    for i in range(1,N):
        if field[i][0] <= h:
            dq.append((i,0))
            check[i][0] = 1
            ret += 1
        if field[i][M-1] <= h:
            dq.append((i,M-1))
            check[i][M-1] = 1
            ret += 1
    while dq:
        if ret >= K: return True
        x,y = dq.popleft()
        for i in range(4):
            dx = x+d[i][0]; dy = y+d[i][1]
            if 0<=dx<N and 0<=dy<M and not(check[dx][dy]) and field[dx][dy] <= h:
                dq.append((dx,dy))
                check[dx][dy] = 1
                ret += 1
    return False

def search(field):
    s,e = 1,1_000_000
    while s < e:
        m = (s+e)//2
        if bfs(field,m):
            e = m
        else:
            s = m+1
    return s

print(search(S))