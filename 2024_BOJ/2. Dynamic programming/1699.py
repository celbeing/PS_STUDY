#1699: 제곱수의 합
import sys
input = sys.stdin.readline
sq = [i**2 for i in range(317)]
N = int(input())
DP = [1e9]*(N+1)
DP[0] = 0
for i in range(1,N+1):
    for t in sq:
        if t > i:
            break
        if DP[i] > DP[i-t]+1:
            DP[i] = DP[i-t]+1
print(DP[N])