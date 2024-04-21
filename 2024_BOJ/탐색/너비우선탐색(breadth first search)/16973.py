#16973: 직사각형 탈출
import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
N,M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
H,W,Sr,Sc,Fr,Fc = map(int,input().split())
Sr -= 1; Sc -= 1; Fr -=1; Fc -=1
check = [[0]*M for _ in range(N)]
check[Sr][Sc] = 1
bfs = deque([(Sr,Sc)])
while bfs:
    x,y = bfs.popleft()
    if x == Fr and y == Fc: break
    for i in range(4):
        dx = x + d[i][0]
        dy = y + d[i][1]
        if 0<=dx<=N-H and 0<=dy<=M-W and not(check[dx][dy]):
            if i == 0:
                for j in range(W):
                    if board[dx+H-1][dy+j]: break
                else:
                    check[dx][dy] = check[x][y]+1
                    bfs.append((dx,dy))
            elif i == 2:
                for j in range(W):
                    if board[dx][dy+j]: break
                else:
                    check[dx][dy] = check[x][y]+1
                    bfs.append((dx,dy))
            elif i == 1:
                for j in range(H):
                    if board[dx+j][dy+W-1]: break
                else:
                    check[dx][dy] = check[x][y]+1
                    bfs.append((dx,dy))
            else:
                for j in range(H):
                    if board[dx+j][dy]: break
                else:
                    check[dx][dy] = check[x][y]+1
                    bfs.append((dx,dy))
        else:
            continue
if check[Fr][Fc]: print(check[Fr][Fc]-1)
else: print(-1)