#C: 수열 회전과 쿼리
import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
A = list(map(int, input().split()))
B = [0]*N
B[0] = A[0]
for i in range(1,N):
    B[i] += B[i - 1] + A[i]
start = 0

for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0] == 1:
        k = q[1]
        start -= k
        if start < 0:
            start += N
    elif q[0] == 2:
        k = q[1]
        start += k
        start %= N
    else:
        a,b = (q[1]-1+start)%N,(q[2]-1+start)%N
        result = B[b] - B[a]
        if a>b:
            result += B[N - 1]
        print(result+A[a])