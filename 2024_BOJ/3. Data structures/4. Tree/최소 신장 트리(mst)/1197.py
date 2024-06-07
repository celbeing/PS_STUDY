#1197: 최소 스패닝 트리
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
edge = []
root = [i for i in range(V+1)]
count = 0
weight = 0

def find(k,parent):
    while parent[k] != k:
        k = parent[k]
    return k

for _ in range(E):
    A,B,C = map(int,input().split())
    edge.append((C,A,B))
edge.sort()
for c, a, b in edge:
    a_root = find(a,root)
    b_root = find(b,root)
    if a_root == b_root: continue
    else:
        if a_root < b_root:
            root[b_root] = a_root
        else:
            root[a_root] = b_root
        count += 1
        weight += c
    if count == V-1: break
print(weight)