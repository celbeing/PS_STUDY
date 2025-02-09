# 1970: 건배
import sys
sys.setrecursionlimit(1500)
input = sys.stdin.readline
n = int(input())
brand = list(map(int, input().split()))
dp = [[-1] * n for _ in range(n)]

def gunbae(a, b):
    if a >= b: return 0
    if dp[a][b] >= 0: return dp[a][b]
    ret = gunbae(a + 1, b)
    for i in range(a + 1 ,b + 1):
        tmp = 0
        if brand[i] == brand[a]:
            tmp = gunbae(a + 1, i - 1) + gunbae(i + 1, b) + 1
            if ret < tmp: ret = tmp
    dp[a][b] = ret
    return ret

result = gunbae(0, n - 1)
print(result)