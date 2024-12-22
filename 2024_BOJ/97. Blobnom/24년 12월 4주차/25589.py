# 25589: 푸앙이와 코인
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    coins = [list(map(int, input().split())) for _ in range(n)]
    quad = [i ** 4 for i in range(400)]
    def net(a, b, k):
        ret = -quad[k]
        ret += coins[a + k][b + k]
        if a >= 0 : ret -= coins[a][b + k]
        if b >= 0: ret -= coins[a + k][b]
        if a >= 0 and b >= 0 : ret += coins[a][b]
        return ret
    l = [0] * n
    r = [0] * n
    u = [0] * n
    d = [0] * n
    for i in range(n):
        for j in range(1, n):
            coins[i][j] += coins[i][j - 1]
    for j in range(n):
        for i in range(1, n):
            coins[i][j] += coins[i - 1][j]

    for k in range(1, 400):
        for i in range(-1, n - k):
            for j in range(-1, n - k):
                sq = net(i, j, k)
                u[i + k] = max(u[i + k], sq)
                d[i + 1] = max(d[i + 1], sq)
                l[j + k] = max(l[j + k], sq)
                r[j + 1] = max(r[j + 1], sq)

    for i in range(1, n):
        if l[i] < l[i - 1]: l[i] = l[i - 1]
        if u[i] < u[i - 1]: u[i] = u[i - 1]
    for i in range(n - 2, -1, -1):
        if r[i] < r[i + 1]: r[i] = r[i + 1]
        if d[i] < d[i + 1]: d[i] = d[i + 1]
    res = 0
    for i in range(1, n):
        if l[i - 1] + r[i] > res:
            res = l[i - 1] + r[i]
        if u[i - 1] + d[i] > res:
            res = u[i - 1] + d[i]
    print(res)
solution()