import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    req = {}
    count = 0
    for i in range(n):
        if a[i] == b[i]: continue
        else:
            count += 1
            if b[i] in req: req[b[i]] += 1
            else: req[b[i]] = 1

    m = int(input())
    d = deque(list(map(int,input().split())))
    remains = False
    for i in range(m):
        now = d.popleft()
        if now in req:
            remains = False
            if req[now] > 0:
                req[now] -= 1
                count -= 1
        elif now not in b:
            remains = True
        else: remains = False
    if count == 0 and not remains: print("YES")
    else: print("NO")