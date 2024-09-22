#1833: 고속도로 설계하기
import sys
input = sys.stdin.readline

def find(parent, k):
    while parent[k] != k:
        k = parent[k]
    return k

def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)
    parent[a] = A
    parent[b] = B
    link = 0
    if A != B:
        parent[B] = a
        link = 1
    return parent, link

def solution():
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    rail = []
    C, M = 0, 0
    install = []
    for i in range(1, N):
        for j in range(i):
            rail.append((cost[i][j], i, j))
            if cost[i][j] < 0: C -= cost[i][j]
    rail.sort()
    parent = [i for i in range(N)]
    for c, i, j in rail:
        parent, link = union(parent, i, j)
        if link and c >= 0:
            C += c
            M += 1
            install.append((i + 1, j + 1))
    print(C, M)
    for m in install:
        print(*m)

solution()