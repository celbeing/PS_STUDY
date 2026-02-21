import random
from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"

def generate_connected_graph(v, extra_edge_prob=0.3):
    if v < 1:
        return []
    nodes = list(range(v))
    random.shuffle(nodes)
    edges = set()
    for i in range(1, v):
        u = nodes[i]
        target = random.choice(nodes[:i])
        weight = random.randint(1, 10)
        edge = tuple(sorted((u, target)))
        edges.add((edge[0], edge[1], weight))
    max_edges = v * (v - 1) // 2
    current_edges = len(edges)
    target_extra = int((max_edges - (v - 1)) * extra_edge_prob)
    count = 0
    while count < target_extra:
        u, target = random.sample(range(v), 2)
        edge_key = tuple(sorted((u, target)))
        existing_keys = set((e[0], e[1]) for e in edges)
        if edge_key not in existing_keys:
            weight = random.randint(1, 10)
            edges.add((edge_key[0], edge_key[1], weight))
            count += 1
            if len(edges) >= max_edges:
                break
    return sorted(list(edges))

for tc in range(49, 51):
    v = randint(20, 20)
    graph = generate_connected_graph(v, extra_edge_prob=1)
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    w = file.writelines(f'{v}\n{len(graph)}\n')

    inf = int(1e9)
    mat = [[inf] * v for _ in range(v)]
    for a, b, c in graph:
        w = file.writelines(f'{a} {b} {c}\n')
        mat[a][b] = c
        mat[b][a] = c

    for k in range(v):
        for i in range(v):
            for j in range(v):
                if i == j: mat[i][j] = 0
                else:
                    if mat[i][k] + mat[k][j] < mat[i][j]:
                        mat[i][j] = mat[i][k] + mat[k][j]
    cost = [sum(mat[i]) for i in range(v)]

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{cost.index(min(cost))}\n')