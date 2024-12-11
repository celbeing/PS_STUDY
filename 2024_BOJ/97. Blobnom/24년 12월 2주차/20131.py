# 20131: 트리 만들기
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    n = int(input())
    count = [0] * (n + 1)
    P = deque(list(map(int, input().split())))
    for p in P: count[p] += 1
    check = [0] * (n + 1)
    tree = []
    for _ in range(n - 2):
        k = 1
        while count[k] or check[k]: k += 1
        if k < P[0]:
            tree.append((k, P[0]))
        else:
            tree.append((P[0], k))
        count[P.popleft()] -= 1
        check[k] = 1
    tree.sort()
    for e in tree:
        print(*e)
solution()