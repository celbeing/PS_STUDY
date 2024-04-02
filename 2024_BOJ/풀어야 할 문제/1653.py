#1653: 양팔 저울
import sys
input = sys.stdin.readline
n = int(input())
w = list(map(int,input().split()))
k = int(input())

dp = [[[0]*116 for _ in range(1<<9)] for _ in range(10)]

def find(i,u,w):
    if w < 0: return 0
    if i == 10 and w == 0: return w
    r = dp[i][u][w]
    if ~r: return r
    r = 0

    left = False
    if i < 5: left = True
    t = abs(i-5)
    if ~left: t += 1

    r += find(i+1,u,w)

    for k in range(n):
        if u & (1<<k)