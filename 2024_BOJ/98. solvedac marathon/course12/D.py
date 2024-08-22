#28017: 게임을 클리어하자
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
t = [list(map(int,input().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
for i in range(M):
     dp[0][i] = t[0][i]
for i in range(1,N):
     if dp[i-1][0] <= dp[i-1][1]:
          fir = 0
          sec = 1
     else:
          fir = 1
          sec = 0
     for j in range(2,M):
          if dp[i-1][fir] >= dp[i-1][j]:
               sec = fir
               fir = j
          elif dp[i-1][sec] >= dp[i-1][j]:
               sec = j
     for j in range(M):
          if j == fir:
               dp[i][j] = t[i][j] + dp[i-1][sec]
          else:
               dp[i][j] = t[i][j] + dp[i-1][fir]
result = int(1e9)
for i in range(M):
     if result > dp[-1][i]: result = dp[-1][i]
print(result)