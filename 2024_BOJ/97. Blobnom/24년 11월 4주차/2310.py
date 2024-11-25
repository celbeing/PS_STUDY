# 2310: 어드벤처 게임
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    while True:
        n = int(input())
        if n == 0: break
        room = [0] * (n + 1)
        link = [[] for _ in range(n + 1)]
        for i in range(1, n + 1):
            inp = list(input().split())
            room[i] = int(inp[1])
            if inp[0] == 'T':
                room[i] *= -1
            link[i] += list(map(int, inp[2:-1]))
        bfs = deque([(1,0)])
        visit = [-1] * (n + 1)
        visit[1] = 0
        while bfs:
            now, money = bfs.popleft()
            if now == n: break
            for next in link[now]:
                d_money = money
                if room[next] > 0:
                    d_money = max(d_money, room[next])
                else:
                    d_money += room[next]
                if d_money <= visit[next]: continue
                visit[next] = d_money
                bfs.append((next, d_money))
        if visit[n] >= 0: print('Yes')
        else: print('No')
solution()