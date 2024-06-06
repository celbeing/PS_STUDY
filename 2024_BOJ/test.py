import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def connect(u, v, capacity=int(1e9)):
    if v in graph[u]:
        capa[u][v] += capacity
    else:
        graph[u].append(v)
        graph[v].append(u)
        capa[u][v] = capacity
        capa[v][u] = 0
        flow[u][v] = 0
        flow[v][u] = 0

def level_graph():
    level = [-1] * (tt + 2)
    level[0] = 0
    queue = deque([0])
    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if level[neighbor] == -1 and capa[current][neighbor] - flow[current][neighbor] > 0:
                queue.append(neighbor)
                level[neighbor] = level[current] + 1
    return level

def dinic(now, flow_value):
    if now == tt + 1:
        return flow_value
    while work[now] < len(graph[now]):
        next_node = graph[now][work[now]]
        residual_capacity = capa[now][next_node] - flow[now][next_node]
        if level[now] + 1 == level[next_node] and residual_capacity > 0:
            min_flow = dinic(next_node, min(flow_value, residual_capacity))
            if min_flow > 0:
                flow[now][next_node] += min_flow
                flow[next_node][now] -= min_flow
                return min_flow
        work[now] += 1
    return 0

T = int(input())
for _ in range(T):
    n = int(input())
    tt = n * 100
    start, goal, steps = map(int, input().split())
    m = int(input())

    graph = defaultdict(list)
    capa = defaultdict(lambda: defaultdict(int))
    flow = defaultdict(lambda: defaultdict(int))

    for u in range(1, n + 1):
        for v in range(-99, -99 + steps):
            connect(u * 100 + v, u * 100 + v + 1)
    connect(0, start * 100 - 99)

    for _ in range(m):
        hospital = int(input())
        if hospital == start:
            connect(0, tt + 1)
        else:
            for k in range(-99, -99 + steps):
                connect(hospital * 100 + k, tt + 1)

    for _ in range(int(input())):
        a, b, p, t = map(int, input().split())
        if a == start:
            connect(0, b * 100 - 100 + t, p)
        limit = min(-99 + steps, -t + 1)
        for k in range(-99, limit):
            connect(a * 100 + k, b * 100 + k + t, p)

    total_flow = 0
    while True:
        level = level_graph()
        if level[-1] == -1:
            break

        work = [0] * (tt + 2)
        while True:
            flow_value = dinic(0, int(1e9))
            if flow_value == 0:
                break
            total_flow += flow_value
            if total_flow >= goal:
                break
        if total_flow >= goal:
            break

    print(min(goal, total_flow))
