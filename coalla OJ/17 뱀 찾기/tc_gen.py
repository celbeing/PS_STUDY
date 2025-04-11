import random
from collections import deque
path = "C:\\Users\\kimsd\\Documents\\GitHub\\2024_BOJ\\coalla OJ\\14 소수판정-2\\"

k = int(input())
n, m = map(int, input().split())
file = open(path + f"{k}.in", 'w+')

graph = dict()
for i in range(1, n + 1):
    graph[i] = []

w = file.writelines(f'{n} {m}\n')
for _ in range(m):
    u, v = map(int, input().split())
    w = file.writelines(f'{u} {v}')
    graph[u].append(v)

count = 0
check = [0] * (n + 1)
bfs = deque()
for i in range(1, n + 1):
    if check[i] == 0:
        flag = True
        bfs.append(i)
        while bfs:
            now = bfs.popleft()
            for next in graph[now]:
                if check[next]:
                    flag = False
                else:
                    bfs.append(next)



file = open(path + f"{k}.out", 'w+')
