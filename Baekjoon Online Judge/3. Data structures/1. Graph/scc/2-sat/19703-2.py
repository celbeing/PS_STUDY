import sys
input = sys.stdin.readline

n, m, a, b = map(int, input().split())

group = [[] for _ in range(m + 1)]
for _ in range(a):
    i, g = map(int, input().split())
    group[g].append(i)

N = (n + a + 5) * 2 + 1
edge = [[] for _ in range(N)]
rev_edge = [[] for _ in range(N)]

node_ptr = 2 * n
for gi in range(1, m + 1):
    lst = group[gi]
    k = len(lst)
    for j in range(k - 1):
        u, v = lst[j], lst[j + 1]
        x1 = node_ptr + 2*j + 1
        x2 = node_ptr + 2*j + 2
        x3 = node_ptr + 2*j + 3
        x4 = node_ptr + 2*j + 4

        edge[u].append(x1);        rev_edge[x1].append(u)
        edge[x1].append(x3);       rev_edge[x3].append(x1)
        edge[x1].append(v + n);    rev_edge[v + n].append(x1)
        edge[x2].append(u + n);    rev_edge[u + n].append(x2)
        edge[x4].append(x2);       rev_edge[x2].append(x4)
        edge[v].append(x2);        rev_edge[x2].append(v)

    node_ptr += k * 2

for _ in range(b):
    i, j = map(int, input().split())
    edge[i + n].append(j);       rev_edge[j].append(i + n)
    edge[j + n].append(i);       rev_edge[i].append(j + n)

visited = [False] * N
order = []

for u in range(1, 2*n + 1):
    if not visited[u]:
        stack = [(u, 0)]
        while stack:
            curr, idx = stack.pop()
            if idx == 0:
                if visited[curr]:
                    continue
                visited[curr] = True
            if idx < len(edge[curr]):
                stack.append((curr, idx + 1))
                v = edge[curr][idx]
                if not visited[v]:
                    stack.append((v, 0))
            else:
                order.append(curr)

visited = [False] * N
scc_num = [0] * N
cid = 0

for u in reversed(order):
    if not visited[u]:
        cid += 1
        stack = [u]
        while stack:
            v = stack.pop()
            if visited[v]:
                continue
            visited[v] = True
            scc_num[v] = cid
            for w in rev_edge[v]:
                if not visited[w]:
                    stack.append(w)

for i in range(1, n + 1):
    if scc_num[i] == scc_num[i + n]:
        print('NIE')
        break
else:
    print('TAK')
