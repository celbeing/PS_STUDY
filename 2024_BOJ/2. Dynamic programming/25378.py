#25378: 조약돌
import sys
input = sys.stdin.readline
N = int(input())
stone = list(map(int,input().split()))
dp = [0]*N
for i in range(N):
    if dp[i] < dp[i-1]: dp[i] = dp[i-1]
    s = stone[i]
    for j in range(i+1,N):
        s = stone[j] - s
        if s < 0: break
        if s == 0:
            if dp[j] < dp[i-1]+1: dp[j] = dp[i-1]+1
            break
print(N-dp[-1])