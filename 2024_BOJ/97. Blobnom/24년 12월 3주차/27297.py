# 27297: 맨해튼에서의 모임
import sys
input = sys.stdin.readline
def solution():
    d, n = map(int, input().split())
    cor = [[0] * n for _ in range(d)]
    for i in range(n):
        loc = list(map(int, input().split()))
        for j in range(d):
            cor[j][i] = loc[j]
    total = 0
    mf = [0] * d
    for i in range(d):
        cor[i].sort()
        mf[i] = cor[i][n // 2]
        for k in cor[i]:
            total += abs(k - mf[i])
    print(total)
    print(*mf)
solution()