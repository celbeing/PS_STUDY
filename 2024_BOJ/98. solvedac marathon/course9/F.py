#25502: 등차수열? 등비수열?
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = list(map(int,input().split()))
dc,db = {},{}
for i in range(1,N):
    c = A[i]-A[i-1]
    b = A[i]//A[i-1]
    br = A[i]%A[i-1]
    dc[c] = dc.get(c,0)+1
    if br == 0: db[b] = db.get(b,0)+1

for _ in range(M):
    i,x = map(int,input().split())
    i -= 1

    if i > 0:
        c = A[i]-A[i-1]
        b = A[i]//A[i-1]
        br = A[i]%A[i-1]
        if dc[c] == 1: dc.pop(c)
        else: dc[c] -= 1
        if br == 0:
            if db[b] == 1: db.pop(b)
            else: db[b] -= 1

    if i < N-1:
        c = A[i+1]-A[i]
        b = A[i+1]//A[i]
        br = A[i+1]%A[i]
        if dc[c] == 1: dc.pop(c)
        else: dc[c] -= 1
        if br == 0:
            if db[b] == 1: db.pop(b)
            else: db[b] -= 1

    A[i] = x
    if i > 0:
        c = A[i]-A[i-1]
        b = A[i]//A[i-1]
        br = A[i]%A[i-1]
        dc[c] = dc.get(c,0)+1
        if br == 0: db[b] = db.get(b,0)+1
    if i < N-1:
        c = A[i+1]-A[i]
        b = A[i+1]//A[i]
        br = A[i+1]%A[i]
        dc[c] = dc.get(c,0)+1
        if br == 0: db[b] = db.get(b,0)+1

    if len(dc.keys()) == 1 and A[-1]>A[0]:
        print("+")
    elif len(db.keys()) == 1 and A[1]%A[0] == 0 and db[A[1]//A[0]] == N-1:
        print("*")
    else:
        print("?")