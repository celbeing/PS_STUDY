# 23086: 두 반으로 나누기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    N, M, K = map(int, input().split())
    friends = [[] for _ in range(N + 1)]
    disconnect = [dict() for _ in range(N + 1)]
    f_list = [0]
    for _ in range(M):
        u, v = map(int, input().split())
        friends[u].append(v)
        friends[v].append(u)
        disconnect[u][v] = K + 1
        disconnect[v][u] = K + 1
        f_list.append((u, v))
    for i in range(1, K + 1):
        u, v = f_list[int(input())]
        disconnect[u][v] = i
        disconnect[v][u] = i

    def is_bipartite(k):
        check = [0] * (N + 1)
        bfs = deque([1])
        check[1] = 1
        count = [1, 0]
        while bfs:
            now = bfs.popleft()
            for next in friends[now]:
                if disconnect[now][next] <= k: continue
                if check[next]:
                    if check[now] == check[next]:
                        return False
                else:
                    check[next] = -check[now]
                    count[1 if check[now] == 1 else 0] += 1
                    bfs.append(next)
        count.sort()
        return count

    s, e = 0, K
    while s < e:
        m = (s + e) // 2
        if is_bipartite(m):
            e = m
        else:
            s = m + 1
    if is_bipartite(s):
        print(s)
        print(*is_bipartite(s))
    else:
        print(-1)
solution()