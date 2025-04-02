# 18858: 훈련소로 가는 날
import sys
input = sys.stdin.readline
def solution():
    n, m = map(int, input().split())
    d = 998244353
    ic = [[0] * (m + 1) for _ in range(n + 1)]
    eq = [[0] * (m + 1) for _ in range(n + 1)]
    dc = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, m + 1):
        eq[1][i] = 1
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            eq[i][j] = ic[i - 1][j] + eq[i - 1][j] + dc[i - 1][j]
            for k in range(1, j):
                ic[i][j] += ic[i - 1][k] + eq[i - 1][k] + dc[i - 1][k]
            for k in range(j + 1, m + 1):
                dc[i][j] += eq[i - 1][k] + dc[i - 1][k]
            ic[i][j] %= d
            eq[i][j] %= d
            dc[i][j] %= d
    res = 0
    for i in range(1, m + 1):
        res += ic[n][i] + eq[n][i] + dc[n][i]
        res %= d
    print(res)
solution()