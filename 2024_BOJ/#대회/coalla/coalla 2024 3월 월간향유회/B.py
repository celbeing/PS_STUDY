#18353: 병사 배치하기
import sys
input = sys.stdin.readline
N = int(input())
p = list(map(int,input().split()))
dp = [0]*N
peek = 0
for i in range(N-1,-1,-1):
    for j in range(N-1,i,-1):
        if dp[i] < dp[j]+1 and p[i] > p[j]:
            dp[i] = dp[j]+1
    if dp[i] == 0:
        dp[i] = 1
    if dp[i] > peek:
        peek = dp[i]
print(N-peek)