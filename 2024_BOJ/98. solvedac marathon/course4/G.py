import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]

N = int(input())
kitchen = [list(input().rstrip()) for _ in range(N)]

blank = 0
for i in range(N):
    for j in range(N):
        if kitchen[i][j] == ".":
            blank += 1

def district(i, j):
    visit = [[0]*N for _ in range(N)]
    dq = deque([(i, j)])
    visit[i][j] = 1

    before = 1
    while dq:
        x,y = dq.popleft()
        for k in range(4):
            dx = x+d[k][0]
            dy = y+d[k][1]
            if 0<=dx<N and 0<=dy<N and not visit[dx][dy] and kitchen[dx][dy] == ".":
                dq.append((dx,dy))
                visit[dx][dy] = 1
                before += 1

    visit = [[0]*N for _ in range(N)]
    visit[i][j] = 1
    dq.clear()
    after = 0
    for k in range(4):
        dx = i+d[k][0]
        dy = j+d[k][1]
        if 0<=dx<N and 0<=dy<N and kitchen[dx][dy] == ".":
            dq.append((dx,dy))
            visit[dx][dy] = 1
            after += 1
            break
    while dq:
        x,y = dq.popleft()
        for k in range(4):
            dx = x+d[k][0]
            dy = y+d[k][1]
            if 0<=dx<N and 0<=dy<N and not visit[dx][dy] and kitchen[dx][dy] == ".":
                dq.append((dx,dy))
                visit[dx][dy] = 1
                after += 1
    if before - 1 == after: return False
    else: return True

result = 0
for i in range(N):
    for j in range(N):
        if kitchen[i][j] == ".":
            if district(i,j): result += 1

print(result)