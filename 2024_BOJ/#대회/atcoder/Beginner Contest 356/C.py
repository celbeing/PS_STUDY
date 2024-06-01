import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

N,M,K = map(int,input().split())
possible = deque(list(combinations(range(1,N+1),K)))
for _ in range(M):
    p = len(possible)
    if p == 0: break
    c = list(input().split())
    C = int(c[0])
    R = c[-1]
    A = sorted(list(map(int,c[1:-1])))
    incase = list(combinations(A, K))
    if R == 'o':
        for i in range(p):
            if possible[0] in incase: possible.append(possible.popleft())
            else: possible.popleft()
    else:
        for i in range(p):
            if possible[0] in incase: possible.popleft()
            else: possible.append(possible.popleft())

print(len(possible))