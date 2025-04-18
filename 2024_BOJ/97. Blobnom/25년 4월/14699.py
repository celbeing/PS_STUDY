# 14699: 관악산 등산
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
def solution():
    n,m = map(int, input().split())
    h = list(map(int, input().split()))
    link = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if h[a] < h[b]:
            link[a].append(b)
        elif h[a] > h[b]:
            link[b].append(a)
    res = [0] * n

    def dfs(node):
        if link[node]:
            count = 0
            for next in link[node]:
                if res[next] == 0:
                    dfs(next)
                if count < res[next]:
                    count = res[next]
            res[node] = count + 1
            return res[node]
        else:
            res[node] = 1
            return 1

    for i in range(n):
        dfs(i)

    for i in range(n):
        print(res[i])
solution()