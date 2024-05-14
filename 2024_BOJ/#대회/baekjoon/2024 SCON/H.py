import sys
input = sys.stdin.readline
N,K = map(int,input().split())
A = [0]*(K*2)+list(map(int,input().split()))+[0]*(K*2)
a,b = 0,K*2-1
w = 0
h = -int(1e9)
for i in range(N+K*2):
    w += A[b+i]
    w -= A[a+i]
    if h < w:
        h = w
print(h)