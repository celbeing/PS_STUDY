import sys
input = sys.stdin.readline
N = int(input())
board = [list(map(int,input().split())) for _ in range(N)]
result = [[0]*N for _ in range(N)]
result[0][0] = board[0][0]
for i in range(1,N):
    result[i][0] = result[i-1][0]*2+board[i][0]
    result[0][i] = result[0][i-1]*2+board[0][i]
for i in range(1,N):
    for j in range(1,N):
        result[i][j] = max(result[i-1][j],result[i][j-1])*2
        result[i][j] += board[i][j]
print(result[-1][-1])