import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
a = 0
b = 0
for i in range(N):
    if A[i] > 9: a*=100
    else: a*=10
    if B[i] > 9: b*=100
    else: b*=10
    a += A[i]
    b += B[i]
if a > b:
    print(b)
else:
    print(a)