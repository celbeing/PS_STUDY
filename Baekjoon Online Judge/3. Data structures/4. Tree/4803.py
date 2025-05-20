#4803: 4. Tree
import sys
from collections import deque
input = sys.stdin.readline
case = 0
while True:
    n,m = map(int,input().split())
    case += 1
    if n==m==0: break
    node = [0 for _ in range(n+1)]
    edge = [[] for _ in range(n+1)]
    count = 0
    flag = True
    tree_finder = deque([(1,0)])
    node[1] = 1
    for _ in range(m):
        u,v = map(int,input().split())
        edge[u].append(v)
        edge[v].append(u)
    while tree_finder:
        now, before = tree_finder.popleft()
        for next in edge[now]:
            if next == before: continue
            if node[next] == 1:
                flag = False
            else:
                node[next] = 1
                tree_finder.append((next,now))
        if not tree_finder:
            if flag:
                count += 1
            flag = True
            for i in range(1, n+1):
                if node[i] == 0:
                    tree_finder.append((i,0))
                    node[i] = 1
                    break
    if count == 0:
        print("Case {}: No trees.".format(case))
    elif count == 1:
        print("Case {}: There is one tree.".format(case))
    else:
        print("Case {}: A forest of {} trees.".format(case,count))