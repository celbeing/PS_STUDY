#15663: N과 M (9)
import sys
from itertools import permutations
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
perm = list(permutations(num,M))
result = set()
for p in perm:
    result.add(p)
for r in sorted(result):
    print(*r)