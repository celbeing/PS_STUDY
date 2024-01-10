#11657: 타임머신
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
inf = 1e9
dp = [inf for _ in range(N+1)]
bus = [list(map(int,input().split())) for _ in range(M)]

def bellmanford(s):
    dp[s] = 0
    for i in range(1,N+1):
        for start, destination, time in bus:
            w = dp[start] + time
            if dp[start] != inf and dp[destination] > w:
                dp[destination] = w
                if i == N:
                    return False
    return True

if bellmanford(1):
    for i in range(2,N+1):
        if dp[i] != inf:
            print(dp[i])
        else:
            print(-1)
else:
    print(-1)