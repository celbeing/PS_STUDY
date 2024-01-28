#15663: N과 M (9)
import sys
from itertools import permutations
input = sys.stdin.readline
N,M = map(int,input().split())
num = list(map(int,input().split()))
perm = list(permutations(num,M))
perm.sort()
result = []
for p in perm:
    if p in result: continue
    result.append(p)
for r in result:
    print(*r)
