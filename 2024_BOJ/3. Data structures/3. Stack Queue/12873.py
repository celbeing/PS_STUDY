# 12873: 기념품
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
P = deque([i for i in range(1,N+1)])
for i in range(1,N):
    m = (i**3-1)%(N-i+1)
    while m > 0:
        P.append(P.popleft())
        m-=1
    P.popleft()
print(P[0])