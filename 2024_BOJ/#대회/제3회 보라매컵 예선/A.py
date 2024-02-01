#A: 대한민국을 지키는 가장 긴 힘
import sys
input = sys.stdin.readline
N = int(input())
S = list(reversed(list(map(int,input().rstrip()))))
dp = [[0,0,0] for _ in range(N)]
for i in range(N):
    if S[i] == 0:
        dp[i] = [5001,5001,5001]
        continue
    for j in range(3):
        if j == 2 and i >= 2:
            t = S[i]*100+S[i-1]*10+S[i-2]
            if t > 641:
                dp[i][2] = 5001
                continue
        min = 5001
        for k in range(3):
            if i-j >= 0 and min > dp[i-j-1][k]:
                min = dp[i-j-1][k]
        dp[i][j] = min+1
result = 0
N -= 1
if dp[N][0] > dp[N][1]:
    if dp[N][1] > dp[N][2]:
        result = dp[N][2]
    else:
        result = dp[N][1]
else:
    if dp[N][0] > dp[N][2]:
        result = dp[N][2]
    else:
        result = dp[N][0]
print(result)