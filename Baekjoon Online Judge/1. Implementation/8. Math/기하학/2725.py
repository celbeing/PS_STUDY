# 2725: 보이는 점의 개수
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

dp = [0] * 1001
dp[1] = 3
for i in range(2, 1001):
    dp[i] = dp[i - 1]
    for j in range(1, i):
        if gcd(i, j) == 1:
            dp[i] += 2

for _ in range(int(input())):
    n = int(input())
    print(dp[n])