#E번 - 트리 탐색기
import sys
from collections import deque
input = sys.stdin.readline
N,Q = map(int,input().split())

folder = [[] for _ in range(N+1)]
toggle = [False for _ in range(N+1)]
toggle[1] = True

for i in range(1,N+1):
    d = list(map(int,input().split()))
    folder[i] = d[1:]

def explore():
    find = []
    dfs = deque([1])
    while dfs:
        now = dfs.pop()
        if now not in find:
            find.append(now)
            if toggle[now]:
                dfs.extend(reversed(folder[now]))
    return find

tree = explore()

cursor = 1
for i in range(Q):
    order = list(input().split())
    if order[0] == "move":
        cursor += int(order[1])
        if cursor < 1:
            cursor = 1
        elif cursor >= len(tree):
            cursor = len(tree)-1
        print(tree[cursor])
    else:
        if toggle[tree[cursor]]:
            toggle[tree[cursor]] = False
        else:
            toggle[tree[cursor]] = True
        tree = explore()