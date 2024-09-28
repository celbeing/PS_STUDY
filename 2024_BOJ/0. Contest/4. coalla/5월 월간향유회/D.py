import sys
from collections import deque
input = sys.stdin.readline
N,K = map(int,input().split())
jp = deque([i for i in range(1,N+1)])
while jp:
    t = jp.popleft()
    jp.append(t)
    for _ in range(K-1):
        jp.popleft()
        if jp[0] == t: break
    if jp[0] == t: break
print(t)