# L: 신촌 도로망 관리와 쿼리
import sys
input = sys.stdin.readline
N,M,Q = map(int,input().split())
roads = []
costs = [0,0,0,0,0]
for _ in range(M):
    v,u,s= input().split()
    v = int(v)
    u = int(u)
    s = ord(s) - ord('A')
    roads.append((u,v,s))

def find(k,r):
    while k != r[k]:
        k = r[k]
    return k

for _ in range(Q):
    costs = list(map(int,input().split()))
    root = [i for i in range(N+1)]
    roads.sort(key = lambda x: costs[x[2]])

    count = 0
    money = 0
    for a,b,r in roads:
        if count == N - 1: break
        root_a = find(a,root)
        root_b = find(b,root)
        if root_a == root_b:
            continue
        if root_a < root_b:
            root[root_b] = root_a
        else:
            root[root_a] = root_b
        count += 1
        money += costs[r]
    print(money)