# 23762: 배드민턴 복식 팀 만들기
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    nn = n >> 2
    m = [0] + sorted(enumerate(list(map(int, input().split()))), key = lambda x: x[1])
    rem = n % 4

    dp = [[0] * (rem + 1) for _ in range(nn + 1)]
    ban = [[0] * (rem + 1) for _ in range(nn + 1)]

    for i in range(1, nn + 1):
        dp[i][0] = dp[i - 1][0] + m[i << 2][1] - m[(i << 2) - 3][1]
    for k in range(1, rem + 1):
        for i in range(1, nn + 1):
            dp[i][k] = dp[i - 1][k] + m[(i << 2) + k][1] - m[(i << 2) - 3 + k][1]
            if dp[i][k] > dp[i][k - 1]:
                ban[i][k] = i
                dp[i][k] = dp[i][k - 1]
            else:
                ban[i][k] = ban[i - 1][k]

    print(dp[-1][-1])
    if rem:
        route = []
        k = nn
        d = rem
        for i in range(rem):
            route.append(m[(ban[k][d] << 2) + d][0])
            k = ban[k][d]
            d -= 1
        route.sort()
        for r in route:
            print(r)
solution()