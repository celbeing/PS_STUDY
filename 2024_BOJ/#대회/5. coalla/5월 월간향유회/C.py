import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
check = [[0]*N for _ in range(N)]
bfs = deque([(0,0)])
check[0][0] = 1
while bfs:
    x,y = bfs.popleft()
    if x == N-1 and y == N-1:
        print("HaruHaru")
        exit()
    dx = x+board[x][y]
    dy = y+board[x][y]
    if dx<N and not check[dx][y]:
        check[dx][y] = 1
        bfs.append((dx,y))
    if dy<N and not check[x][dy]:
        check[x][dy] = 1
        bfs.append((x,dy))
print("Hing")