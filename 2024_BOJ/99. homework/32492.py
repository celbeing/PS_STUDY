#32492: WALK
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    road = [dict() for _ in range(N + 1)]
    dist = [0] * (N + 1)
    time = [0] * (N + 1)
    for _ in range(M):
        a, b, c = map(int, input().split())
        road[a][b] = c
        road[b][a] = c
    bfs = [(1, 0, 1)]
    while bfs:
        d, t, now = heappop(bfs)
        for next in road[now]:
            if road[now][next] > t and (dist[next] < d or time[next] > t):
                heappush(bfs, (d + 1, road[now][next], next))
                time[next] = road[now][next]
                dist[next] = d
    print(*dist[1:])
solution()

'''
4 5
1 2 1
2 3 3
2 4 2
3 4 4
1 4 1
>> 0 2 3 4

4 5
1 2 1
2 3 3
2 4 2
3 4 4
1 4 5
>> 4 1 3 3

5 8
1 2 1
1 4 7
1 5 6
2 3 3
2 5 2
3 4 4
3 5 3
4 5 5
>> 6 1 3 7 5

5 10
1 2 1
1 3 7
1 4 10
1 5 8
2 3 2
2 4 5
2 5 4
3 4 6
3 5 3
4 5 9
>> 10 4 6 9 8

5 7
1 2 1
1 3 1
2 5 4
2 4 5
3 4 2
3 5 2
5 4 3
>> 0 4 1 5 3
'''