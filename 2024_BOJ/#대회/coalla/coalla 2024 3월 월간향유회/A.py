#1987: 알파벳
import sys
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
A = ord('A')
R,C = map(int,input().split())
board = [list(input().rstrip()) for _ in range(R)]
maximum = 0
limit = 0
for i in range(R):
    for j in range(C):
        maximum |= 1<<(ord(board[i][j])-A)
for i in range(26):
    if maximum & 1<<i:
        limit += 1
peek = 0
dfs = [(0,0,1,1<<(ord(board[0][0])-A))]
while dfs:
    x,y,count,path = dfs.pop()
    if peek < count:
        peek = count
    if peek == limit: break
    for i in range(4):
        dx = x + d[i][0]
        dy = y + d[i][1]
        if 0 <= dx < R and 0 <= dy < C:
            t = 1 << (ord(board[dx][dy]) - A)
            if  t & path:
                continue
            dfs.append((dx, dy, count+1, path | t))

print(peek)