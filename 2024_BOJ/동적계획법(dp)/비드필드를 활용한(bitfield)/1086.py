#1086: 박성원
import sys
from math import gcd, factorial
input = sys.stdin.readline
def dfs(dgt, mask, r):
    if mask == (1 << N) - 1:
        if r == 0:
            return 1
        else:
            return 0

    if dp[mask][r] >= 0:
        return dp[mask][r]

    for i in range(N):
        if mask & (1 << i): continue
        dp[mask][r] += dfs(dgt + digit[i], mask | 1 << i, (r+remain[i][dgt])%K)
    dp[mask][r] += 1
    return dp[mask][r]

N = int(input())
n = [int(input()) for _ in range(N)]
K = int(input())
dp = [[-1] * K for _ in range(1<<N)]
digit = []
for a in n:
    digit.append(len(str(a)))
remain = [[n[i]%K] for i in range(N)]
for i in range(N):
    for j in range(1,sum(digit)):
        remain[i].append(remain[i][j-1]*10%K)

case = dfs(0,0,0)
if case == 0:
    print("0/1")
else:
    nf = factorial(N)
    g = gcd(nf,case)
    print("{}/{}".format(case//g,nf//g))