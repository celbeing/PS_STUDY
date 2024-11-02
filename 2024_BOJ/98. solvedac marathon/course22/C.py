#8564: Inwestycja
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N = int(input())
    graph = [deque() for _ in range(N + 1)] # 트리를 관리하는 덱
    subtree = [0] * (N + 1)     # 현재 노드를 루트로 하는 서브트리의 정점 수
    parent = [0] * (N + 1)      # 현재 노드의 부모 노드
    edge_cnt = [0] * (N + 1)    # 현재 노드에 연결된 노드의 수

    # 트리 생성
    for _ in range(N - 1):
        v, w = map(int, input().split())
        graph[v].append(w)
        graph[w].append(v)
        edge_cnt[v] += 1
        edge_cnt[w] += 1

    # 트리 탐색(루트는 1)
    now = 1
    edge_cnt[1] += 1
    while edge_cnt[now]:
        # 연결된 노드의 수가 하나 뿐이면 부모 노드에 subtree 값 넘기고
        # 부모 노드로 탐색 옮기기
        if edge_cnt[now] == 1:
            subtree[now] += 1
            subtree[parent[now]] += subtree[now]
            now = parent[now]
        # 아니면 자식 노드로 탐색 이어가기
        else:
            # 탐색하려는 노드가 부모 노드라면 연결된 노드 덱의 맨 앞으로 보내기
            if graph[now][-1] == parent[now]: graph[now].appendleft(graph[now].pop())
            # 현재 노드의 연결된 노드 수 1 줄이고
            # 탐색하려는 자식 노드의 부모 노드를 현재 노드로 바꾸기
            # 탐색 노드를 자식 노드로 바꾸면서 부모 노드와 연결된 자식 노드 삭제
            else:
                edge_cnt[now] -= 1
                parent[graph[now][-1]] = now
                now = graph[now].pop()
    res = 0
    for i in range(2, N + 1):
        res = max(res, subtree[i] * (N - subtree[i]))
    print(res)
solution()