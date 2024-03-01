#C: 당근 클릭 게임
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
store = [tuple(map(int,input().split())) for _ in range(N)]
store.sort()
dp = [[-1 for _ in range(5001)] for _ in range(K+1)]
dp[0][1] = 0
highspeed = 1
for i in range(K):
    for j in range(1, highspeed+1):
        if dp[i+1][j] == -1 or dp[i+1][j] < dp[i][j]+j:
            dp[i+1][j] = dp[i][j] + j
            for cost, increase in store:
                if cost > dp[i][j]: break
                if dp[i+1][j+increase] == -1 or dp[i+1][j+increase] < dp[i][j]-cost:
                    dp[i+1][j+increase] = dp[i][j]-cost
                    if j+increase > highspeed:
                        highspeed = j+increase

maximum = 0
for k in dp[K]:
    if k > maximum:
        maximum = k

print(maximum)