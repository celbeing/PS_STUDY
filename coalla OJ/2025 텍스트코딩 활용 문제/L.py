import random
from random import randint
from collections import deque
check = set()
path = r"C:\Users\kimsd\OneDrive\Documents\GitHub\PS_STUDY\coalla OJ\2025 텍스트코딩 활용 문제\\"

def generate_dag_single_source(v, extra_edge_prob=0.3):
    if v < 1:
        return []

    # 1. 위상 정렬 순서(Topological Order) 생성
    # 0번 정점은 무조건 맨 앞에 고정 (진입차수 0인 유일한 정점)
    # 나머지 정점들은 랜덤하게 섞어서 뒤에 배치
    others = list(range(1, v))
    random.shuffle(others)
    topo_order = [0] + others

    edges = set()  # 중복 확인용 (u, v)
    edge_list = []  # 결과 저장용 (u, v, w)

    # 2. 필수 간선 연결 (Backbone)
    # 0번을 제외한 모든 노드가 최소 1개의 진입 간선을 갖도록 보장
    for i in range(1, v):
        target = topo_order[i]

        # 현재 노드(target)보다 위상 정렬 순서가 앞선 노드들 중 하나를 랜덤 선택
        possible_parents = topo_order[:i]
        source = random.choice(possible_parents)

        weight = random.randint(1, 10)
        edges.add((source, target))
        edge_list.append((source, target, weight))

    # 3. 추가 간선 연결 (Random Edges)
    # 위상 정렬 순서를 지키는 선에서(source_idx < target_idx) 랜덤하게 간선 추가
    # 이렇게 하면 절대 사이클이 발생하지 않음
    for i in range(v):
        for j in range(i + 1, v):
            source = topo_order[i]
            target = topo_order[j]

            # 이미 존재하는 간선은 패스
            if (source, target) in edges:
                continue

            # 확률적으로 간선 추가
            if random.random() < extra_edge_prob:
                weight = random.randint(1, 10)
                edges.add((source, target))
                edge_list.append((source, target, weight))

    # 4. 정렬하여 반환 (보기 좋게)
    return sorted(edge_list)

def dfs(now, route, cost):
    if len(g[now]):
        for next in g[now]:
            if check[next] == 0:
                check[next] = 1
                dfs(next, route + [next], cost + g[now][next])
                check[next] = 0
    else:
        res.append((-cost, len(route), route))
        return

for tc in range(1,51):
    v = randint(20, 20)
    graph = generate_dag_single_source(v, extra_edge_prob=0.8)
    e = len(graph)
    res = []
    check = [0] * v
    file = open(path + f'{tc}.in', 'w+', encoding='utf-8')
    g = [dict() for _ in range(v)]
    w = file.writelines(f'{v}\n{e}\n')
    for a, b, c in graph:
        w = file.writelines(f'{a} {b} {c}\n')
        g[a][b] = c
    check[0] = 1
    dfs(0, [0], 0)
    res.sort()

    file = open(path + f'{tc}.out', 'w+', encoding = 'utf-8')
    w = file.writelines(f'{-res[0][0]}\n{' '.join(map(str, res[0][2]))}\n')