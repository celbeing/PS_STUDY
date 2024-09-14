#25419: 정수를 끝까지 외치자
import sys
input = sys.stdin.readline
def solution():
    n, k = map(int, input().split())
    block = list(map(int, input().split()))
    dp = [0] * (n + 1)
    for b in block: dp[b] = 2
    l = n
    cnt = k
    for i in range(n, -1, -1):
        if dp[i]: cnt += 1
        else:
            if cnt >= k:
                l = i
            cnt = 0
    dp[l] = 1
    for i in range(l - 1, 0, -1):
        if dp[i] == 2: continue
        for j in range(i + 1, min(i + k, n) + 1):
            if dp[j] == 1:
                dp[i] = 0
                break
        else: dp[i] = 1
    for i in range(1, min(n, k) + 1):
        if dp[i] == 1:
            return 1
    else: return 0
print(solution())