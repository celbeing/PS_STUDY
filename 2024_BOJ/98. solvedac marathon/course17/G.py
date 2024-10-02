#2611: 자동차 경주
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N = int(input())
    road = [dict() for _ in range(N + 1)]
    dp = [0] * (N + 1)
    tp_sort = deque([1])
    income = [0] * (N + 1)
    to = [-1] * (N + 1)
    for _ in range(int(input())):
        p, q, r = map(int, input().split())
        if q == 1: q = 0
        road[p][q] = max(road[p].get(q, 0), r)
        income[q] += 1
    while tp_sort:
        now = tp_sort.popleft()
        for next in road[now]:
            income[next] -= 1
            if income[next] == 0:
                tp_sort.append(next)
            k = dp[now] + road[now][next]
            if dp[next] < k:
                dp[next] = k
                to[next] = now
    route = []
    k = 0
    while k >= 0:
        route.append(k)
        k = to[k]
    route[0] = 1
    route.reverse()
    print(dp[0])
    print(*route)
solution()