# 20131: 트리 만들기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    count = [0] * (n + 1)
    P = deque(list(map(int, input().split())))
    for p in P: count[p] += 1
    tree = []
    head = [i for i in range(n + 1)]

    def find(k):
        while k != head[k]:
            k = head[k]
        return k

    def union(a, b):
        B = find(b)
        head[a] = B
        return 0

    for _ in range(n - 2):
        k = find(n)
        while count[k]:
            k -= 1
            k = find(k)
        if k < P[0]:
            tree.append((k, P[0]))
        else:
            tree.append((P[0], k))
        count[P.popleft()] -= 1
        union(k, k - 1)
    a = find(n)
    union(a, a - 1)
    b = find(n)
    tree.append((b, a))
    tree.sort()
    for e in tree:
        print(*e)
solution()