import sys
input = sys.stdin.readline

def solution(S):
    last = dict()
    N = len(S)
    dp = [0]*(N+1)
    dp[0] = 1
    for i in range(1,N+1):
        dp[i] = dp[i-1] << 1
        if S[i-1] in last:
            dp[i] -= dp[last[S[i-1]]-1]
        last[S[i-1]] = i
    return dp[-1]



T = int(input())
for _ in range(T):
    print(solution(input().rstrip()))