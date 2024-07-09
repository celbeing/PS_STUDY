import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = list(map(int,input().split()))

s,e = -1,0
p = A[0]
count = 0
while True:
    if p == M:
        count += 1
        e += 1
        if e == N: break
        p += A[e]
    elif p < M:
        e += 1
        if e == N: break
        p += A[e]
    else:
        s += 1
        p -= A[s]
print(count)