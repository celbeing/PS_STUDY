import sys
input = sys.stdin.readline
N,M = map(int,input().split())
castle = [list(input().rstrip()) for _ in range(N)]
vert,hori = 0,0
for i in range(N):
    for j in range(M):
        if castle[i][j] == 'X': break
    else: hori += 1
for i in range(M):
    for j in range(N):
        if castle[j][i] == 'X': break
    else: vert += 1
print(max(vert,hori))