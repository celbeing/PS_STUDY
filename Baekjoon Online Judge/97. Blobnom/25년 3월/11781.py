# 11781: 퇴근 시간
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n, m, s, e = map(int, input().split())
    road = [dict() for _ in range(n + 1)]
    inf = int(1e15)
    check = [inf] * (n + 1)

    for _ in range(m):
        a, b, l, t1, t2 = map(int, input().split())
        road[a][b] = (l, t1)
        road[b][a] = (l, t2)
    check[0] = check[1] = 0
    hq = []
    heappush(hq, (0, 1))
    while hq:
        time, now = heappop(hq)
        for next in road[now]:
            dist, rush = road[now][next]
            new_time = 0
            if rush:
                if time <= s:
                    if time + dist <= s: new_time = dist
                    else:
                        new_time = s - time
                        dist -= new_time
                        if e - s <= dist * 2:
                            dist -= (e - s) / 2
                            new_time += e - s + dist
                        else:
                            new_time += dist * 2
                elif s < time <= e:
                    if time + dist * 2 <= e: new_time = dist * 2
                    else:
                        new_time = e - time
                        dist -= new_time / 2
                        new_time += dist
                else:
                    new_time = dist
            else:
                new_time = dist
            new_time += time
            if check[next] > new_time:
                heappush(hq,(new_time, next))
                check[next] = new_time
    result = max(check)
    if int(result) == result:
        print(int(result))
    else:
        print(result)
solution()