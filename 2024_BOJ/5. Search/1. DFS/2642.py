# 2642: 전개도
import sys
input = sys.stdin.readline
d = [(-1,0),(0,1),(1,0),(0,-1)]

board = [list(map(int,input().split())) for _ in range(6)]
visit = [[0]*6 for _ in range(6)]
cube = [0]*6
dir = 0

def turn(dir):
    tmp = cube[0]
    if dir == 0:
        cube[0] = cube[3]
        cube[3] = cube[5]
        cube[5] = cube[1]
        cube[1] = tmp
    elif dir == 1:
        cube[0] = cube[2]
        cube[2] = cube[5]
        cube[5] = cube[4]
        cube[4] = tmp
    elif dir == 2:
        cube[0] = cube[1]
        cube[1] = cube[5]
        cube[5] = cube[3]
        cube[3] = tmp
    else:
        cube[0] = cube[4]
        cube[4] = cube[5]
        cube[5] = cube[2]
        cube[2] = tmp

def dfs(x,y):
    for i in range(4):
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<6 and 0<=dy<6 and not visit[dx][dy] and board[dx][dy]:
            visit[dx][dy] = 1
            turn(i)
            if cube[0]: return False
            cube[0] = board[dx][dy]
            if not dfs(dx,dy): return False
            turn((i+2)%4)
    return True

def check():
    count = 0
    for i in range(36):
        if board[i//6][i%6]: count += 1
    if count == 6: pass
    else: return False
    if sorted(cube) == [1,2,3,4,5,6]: pass
    else: return False
    return True

x,y = 0,0
for i in range(36):
    if board[i//6][i%6]:
        x = i//6
        y = i%6
        visit[x][y] = 1
        cube[0] = board[x][y]
        break

dfs(x,y)
if check():
    t = cube.index(1)
    if t == 0: print(cube[5])
    elif t == 1: print(cube[3])
    elif t == 2: print(cube[4])
    elif t == 3: print(cube[1])
    elif t == 4: print(cube[2])
    else: print(cube[0])
else: print(0)