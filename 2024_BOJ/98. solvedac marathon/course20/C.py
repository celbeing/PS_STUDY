#2479: 경로 찾기
import sys
from collections import deque
input = sys.stdin.readline
def hamming_dist(a, b, K):
    ret = 0
    for i in range(K):
        ret += 0 if a[i] == b[i] else 1
    return ret
def solution():
    N, K = map(int, input().split())
    link = [[] for _ in range(N + 1)]
    visit = [0] * (N + 1)
    code = [0]
    for i in range(1, N + 1):
        code.append(input().rstrip())
        for j in range(1, i):
            if hamming_dist(code[i], code[j], K) == 1:
                link[i].append(j)
                link[j].append(i)
    A, B = map(int, input().split())
    visit[A] = -1
    bfs = deque([A])
    while bfs:
        now = bfs.popleft()
        for next in link[now]:
            if visit[next] == 0:
                visit[next] = now
                bfs.append(next)
    if visit[B] == 0:
        print(-1)
    else:
        route = []
        k = B
        while k > 0:
            route.append(k)
            k = visit[k]
        route.reverse()
        print(*route)
solution()