#1043: 거짓말
import sys
input = sys.stdin.readline
def find(k, parent):
    while parent[k] != k:
        k = parent[k]
    return k

def union(a, b, parent):
    A = find(a, parent)
    B = find(b, parent)
    parent[a] = A
    parent[b] = B
    if A < B:
        parent[B] = A
    else:
        parent[A] = B
    return parent

def solution():
    N, M = map(int, input().split())
    known = list(map(int, input().split()))[1:]
    parent = [i for i in range(51)]
    for k in known: parent[k] = 0
    party = [list(map(int, input().split())) for _ in range(M)]
    for p in party:
        for i in p[2:]:
            parent = union(p[1], i, parent)

    johnsnow = 0
    for p in party:
        for i in p[1:]:
            if find(i, parent) == 0: break
        else:
            johnsnow += 1
    print(johnsnow)
solution()