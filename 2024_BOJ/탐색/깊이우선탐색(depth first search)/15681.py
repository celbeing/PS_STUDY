#15681: 트리와 쿼리
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N,R,Q = map(int,input().split())
graph = [[] for _ in range(N+1)]
tree = [0 for _ in range(N+1)]
check = [True for _ in range(N+1)]
for _ in range(1,N):
    U,V = map(int,input().split())
    graph[U].append(V)
    graph[V].append(U)

def subtree(p):
    check[p] = False
    while graph[p]:
        node = graph[p].pop()
        if check[node]:
            tree[p] += subtree(node)
    tree[p] += 1
    return tree[p]

subtree(R)

for _ in range(Q):
    print(tree[int(input())])