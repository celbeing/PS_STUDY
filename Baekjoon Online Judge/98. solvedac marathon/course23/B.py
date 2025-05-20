#5992: The Leisurely Stroll
import sys
from collections import deque
input = sys.stdin.readline
def solution():
    P = int(input())
    tree = [[] for _ in range(P)]
    for _ in range(P - 1):
        C, D1, D2 = map(int, input().split())
        tree[C] += [D1, D2]
    bfs = deque([(1,1)])
    far = 0
    while bfs:
        node, depth = bfs.popleft()
        for next in tree[node]:
            if next:
                bfs.append((next, depth + 1))
            else:
                far = depth
    print(far)
solution()