# 20131: 트리 만들기
import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n = int(input())
    count = [0] * (n + 1)
    P = deque(list(map(int, input().split())))
    for p in P: count[p] += 1
    tree = []
    L = []
    for i in range(1, n + 1):
        if count[i] == 0: heappush(L, -i)

    for _ in range(n - 2):
        l = -heappop(L)
        if P[0] > l:
            tree.append((l, P[0]))
        else:
            tree.append((P[0], l))
        count[P[0]] -= 1
        if count[P[0]] == 0:
            heappush(L, -P[0])
        P.popleft()

    tree.append((-L[1], -L[0]))
    tree.sort()
    for e in tree:
        print(*e)
solution()