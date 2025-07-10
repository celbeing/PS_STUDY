# 33928: 나이트 오브 나이츠(Hard)
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

def link(u, v, f = 1, c = 0):
    capa[u][v], capa[v][u] = f, 0
    flow[u][v], flow[v][u] = 0, 0
    cost[u][v], cost[v][u] = c, -c

n = int(input())
board = [list(map(int, input().split()))]

node = n * n
s = node * 2
t = s + 1

capa = [dict() for _ in range(t + 1)]
flow = [dict() for _ in range(t + 1)]
cost = [dict() for _ in range(t + 1)]

x, y = 0, 0
for i in range(node):
    if y == n:
        x += 1
        y = 0
    link(s, i, 5)
