#26607: 시로코와 은행털기
import sys
input = sys.stdin.readline
n,k,x = map(int,input().split())
stat = [tuple(map(int,input().split())) for _ in range(n)]

dp = [[0]*(n*x+1) for _ in range(k+1)]
dp[0][0] = 1

for a,b in stat:
    for i in range(k,0,-1):
        for j in range(a,n*x):
            if dp[i-1][j-a]:
                dp[i][j] = 1

res = 0
for j in range(n*x):
    if dp[k][j]:
        if j*(k*x-j) > res:
            res = j*(k*x-j)
print(res)