import sys
input = sys.stdin.readline
N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
i = mat[0][0]-1
for j in range(1,N):
    if i >= j:
        i = mat[i][j]-1
    else:
        i = mat[j][i]-1
print(i+1)