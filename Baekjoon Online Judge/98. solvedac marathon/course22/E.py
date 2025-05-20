#30050: 트리와 쿼리 10^9
import sys
from collections import defaultdict
input = sys.stdin.readline
def solution():
    tree = dict()
    for _ in range(int(input())):
        q, a, b = map(int, input().split())
        if q == 1:
            tree[b] = a
        else:
            path_a = defaultdict(int)
            path_b = defaultdict(int)
            while a:
                path_a[a] += a
                path_a[tree.get(a, a // 2)] = path_a[a]
                a = tree.get(a, a // 2)
            while b:
                if path_a[b]: break
                path_b[b] += b
                path_b[tree.get(b, b // 2)] = path_b[b]
                b = tree.get(b, b // 2)
            print(path_a[b] + path_b[b])
solution()