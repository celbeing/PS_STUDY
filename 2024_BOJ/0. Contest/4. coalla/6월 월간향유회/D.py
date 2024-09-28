import sys
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
board = [list(map(int,input().split())) for _ in range(5)]
visit = [[0]*5 for _ in range(5)]
r,c = map(int,input().split())

def dfs(x,y,k,m):
    if k == 2: return 1
    elif m == 3: return 0
    for i in range(4):
        dx,dy = x+d[i][0],y+d[i][1]
        if 0<=dx<5 and 0<=dy<5 and board[dx][dy] > -1 and visit[dx][dy] == 0:
            visit[dx][dy] = 1
            if board[dx][dy] == 1:
                if dfs(dx,dy,k+1,m+1):
                    return 1
            else:
                if dfs(dx,dy,k,m+1):
                    return 1
            visit[dx][dy] = 0
    return 0
visit[r][c] = 1
print(dfs(r,c,0,0))