import sys
input = sys.stdin.readline

N,P,Q = map(int,input().split())
A = []
B = []
if P >= Q:
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
else:
    B = list(map(int,input().split()))
    A = list(map(int,input().split()))
    t = P
    P = Q
    Q = t
R = [0]*N
c = P-Q
result = 0
for i in range(N):
    t = B[i]-A[i]
    if t == 0: continue
    elif t > 0 and t % c == 0:
        R[i] = t // c
        result += R[i]
    else:
        result = 10001
        break
if result <= 10000:
    print("YES")
    print(*R)
else:
    print("NO")
