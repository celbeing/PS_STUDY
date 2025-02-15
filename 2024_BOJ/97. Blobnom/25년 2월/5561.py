# 5561: 과자의 분할
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    p = [0] * n
    for i in range(1, n):
        p[i] = int(input())
    inf = int(1e8)
    cost = [inf] * (n + 1)
    cost[1] = 0
    for i in range(2, n + 1):
        i_cost = [inf] * (i + 1)
        for j in range(1, i + 1):
            i_cost[j] = cost[j - 1]
            if i_cost[j] > cost[i - j] + p[i - 1]:
                i_cost[j] = cost[i - j] + p[i - 1]
        for j in range(1, i + 1):
            cost[j] = i_cost[j]
    print(cost[n // 2])
solution()