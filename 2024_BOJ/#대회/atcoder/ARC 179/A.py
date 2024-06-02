import sys
input = sys.stdin.readline
N,K = map(int,input().split())
A = sorted(list(map(int,input().split())))
t = sum(A)
sum = 0
less = False
more = False
if sum < K:
    less = True
    for k in A:
        sum += k
        if sum >= K:
            less = False
            more = True
        elif more and sum < K:
            more = False
            break
    if less | more:
        print("Yes")
        print(*A)
    else:
        print("No")
else:
    if t < K: print("No")
    else:
        print("Yes")
        print(*reversed(A))