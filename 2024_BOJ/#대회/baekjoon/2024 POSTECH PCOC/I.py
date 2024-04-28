# I: 78계단 내려가기 대회
import sys
input = sys.stdin.readline
N = int(input())
H = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
dp = [0]*N
for i in range(1,N):
    dp[i] = dp[i-1]
    s,e = 1,i
    while s < e:
        m = (s+e)//2
        if H[m]-H[i] < B[i-1]:
            e = m
        else:
            s = m+1

    if H[s-1]-H[i] < B[i-1]: continue
    k = dp[s-1] + A[i-1]
    if k > dp[i]:
        dp[i] = k
print(dp[-1])