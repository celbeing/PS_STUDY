#12763: 지각하면 안 돼
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n = int(input())
    t, m = map(int, input().split())
    graph = [dict() for _ in range(n + 1)]
    hq = []   # (t, m, n)
    heappush(hq, (0, 0, 1))
    rec = [10000] * (n + 1)
    visit = [(10000, 10000)] * (n + 1)
    rec[1] = 0
    visit[1] = (0, 0)
    for _ in range(int(input())):
        u, v, time, money = map(int, input().split())
        graph[u][v] = (time, money)
        graph[v][u] = (time, money)
    while hq:
        now_t, now_m, now = heappop(hq)
        for next in graph[now]:
            new_t = now_t + graph[now][next][0]
            new_m = now_m + graph[now][next][1]
            if new_t > t or new_m > m: continue
            if new_t > visit[next][0] and new_m > visit[next][1]: continue
            elif new_t < visit[next][0] and new_m < visit[next][1]:
                visit[next] = (new_t, new_m)
            if rec[next] > new_m:
                rec[next] = new_m
            heappush(hq, (new_t, new_m, next))
    if rec[n] == 10000: print(-1)
    else: print(rec[n])
solution()