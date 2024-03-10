#E: 전역 역전
import sys
from datetime import datetime
input = sys.stdin.readline
y,m,d = map(int,input().split())
jh = datetime(y,m,d)
y,m,d = map(int,input().split())
yd = datetime(y,m,d)
gap = (yd-jh).days
T,N = map(int,input().split())
plans = []
for _ in range(N):
    n,C,K = map(int,input().split())
    if n == 3:
        plans.append((C,K*30))
    else:
        plans.append((C,K))
dp = [[0]*(T+1) for _ in range(N+1)]
for i in range(1,N+1):
    c,k = plans[i-1]
    for j in range(1,T+1):
        if j>=c:
            dp[i][j] = max(dp[i-1][j-c]+k, dp[i-1][j])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
print(abs(gap - dp[N][T]))