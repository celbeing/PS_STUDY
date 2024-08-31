#24428: 알고리즘 수업 - 행렬 경로 문제 5
import sys
input = sys.stdin.readline
n = int(input())
mat = [[0]*(n+1)]
for _ in range(n):
    mat.append([0]+list(map(int,input().split())))
P = int(input())
check = [[0]*(n+1) for _ in range(n+1)]
for _ in range(P):
    x,y = map(int,input().split())
    check[x][y] = 1
score = [[[0]*4 for _ in range(n+1)] for _ in range(n+1)]
score[1][1][0] = mat[1][1]
for i in range(2,n+1):
    for j in range(i):
        if check[i-j][j+1]:
            for k in range(3):
                if score[i-j-1][j+1][k] or score[i-j][j][k]:
                    score[i-j][j+1][k+1] = max(score[i-j-1][j+1][k],score[i-j][j][k])+mat[i-j][j+1]
            if score[i-j-1][j+1][3] or score[i-j][j][3]:
                score[i-j][j+1][3] = max(score[i-j][j+1][3],max(score[i-j-1][j+1][3],score[i-j][j][3])+mat[i-j][j+1])
        else:
            for k in range(4):
                if score[i-j-1][j+1][k] or score[i-j][j][k]:
                    score[i-j][j+1][k] = max(score[i-j-1][j+1][k],score[i-j][j][k])+mat[i-j][j+1]
for j in range(2,n+1):
    for i in range(n,j-1,-1):
        if check[i][n-i+j]:
            for k in range(3):
                if score[i-1][n-i+j][k] or score[i][n-i+j-1][k]:
                    score[i][n-i+j][k+1] = max(score[i-1][n-i+j][k],score[i][n-i+j-1][k])+mat[i][n-i+j]
            if score[i-1][n-i+j][3] or score[i][n-i+j-1][3]:
                score[i][n-i+j][3] = max(score[i][n-i+j][3],max(score[i-1][n-i+j][3],score[i][n-i+j-1][3])+mat[i][n-i+j])
        else:
            for k in range(4):
                if score[i-1][n-i+j][k] or score[i][n-i+j-1][k]:
                    score[i][n-i+j][k] = max(score[i-1][n-i+j][k],score[i][n-i+j-1][k])+mat[i][n-i+j]
if score[n][n][3]:
    print(score[n][n][3])
else:
    print(-1)
