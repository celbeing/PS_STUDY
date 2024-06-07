import sys
input = sys.stdin.readline
N = int(input())
key = ['M','O','B','I','S']
d = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
board = [list(input().rstrip()) for _ in range(N)]
count = 0

for x in range(N):
    for y in range(N):
        for k in range(8):
            dx = x
            dy = y
            for t in range(5):
                if 0<=dx<N and 0<=dy<N and board[dx][dy] == key[t]:
                    dx += d[k][0]
                    dy += d[k][1]
                else:
                    break
            else:
                count += 1

print(count)