#4384: 공평하게 팀 나누기
import sys
input = sys.stdin.readline
N = int(input())
K = [int(input()) for _ in range(N)]
total = sum(K)
gap = total
half = N // 2
dp = [[0] * (total//2+451) for _ in range(half + 1)]
dp[0][0] = 1
for n in K:
    for i in range(half,0,-1):
        for k in range(n,total//2+451):
            if dp[i-1][k-n]:
                dp[i][k] = 1
                continue
a = 0
for k in range(total//2+451):
    if dp[half][k]:
        if gap > abs(total-k*2):
            gap = abs(total-k*2)
            a = k
if a>total-a:
    a = total - a
print(a, total-a)