# 16202: MST 게임
import sys
input = sys.stdin.readline
def solution():
    n, m, k = map(int, input().split())
    edge = [0] + [tuple(map(int, input().split())) for _ in range(m)]
    head = []
    result = []

    def find(k):
        t = k
        while t != head[t]:
            t = head[t]
        while k != head[k]:
            p = head[k]
            head[k] = t
            k = p
        return k

    def union(a, b):
        A = find(a)
        B = find(b)
        if A < B:
            head[B] = A
        else:
            head[A] = B
        return 0

    for turn in range(1, k + 1):
        head = [i for i in range(n + 1)]
        count = 0
        score = 0
        for now in range(turn, m + 1):
            x, y = edge[now]
            if find(x) == find(y): continue
            union(x, y)
            count += 1
            score += now
        if count == n - 1:
            result.append(score)
        else: break
    result += [0] * (k - len(result))
    print(*result)
solution()