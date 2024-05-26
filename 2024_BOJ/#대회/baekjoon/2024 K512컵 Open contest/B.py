import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
com = [0]*(N+1)
infest = N
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        if com[q[1]] == 0: infest -= 1
        com[q[1]] = 1
    elif q[0] == 2:
        if com[q[1]]: infest += 1
        com[q[1]] = 0
    else:
        print(infest)