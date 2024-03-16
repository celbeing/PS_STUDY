#1311: 할 일 정하기 1
import sys
input = sys.stdin.readline
inf = int(1e9)
N = int(input())
D = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1]*((1<<N)-1) for _ in range(N)]

def dfs(x,mask):
    if mask == (1<<N)-1: return 0
    if dp[x][mask] > 0: return dp[x][mask]

    dp[x][mask] = inf
    for i in range(N):
        if mask & (1<<i): continue
        dp[x][mask] = min(dp[x][mask],dfs(x+1,mask|(1<<i))+D[x][i])
    return dp[x][mask]

print(dfs(0,0))