import sys
input = sys.stdin.readline
N,H = map(int,input().split())
d = list(map(int,input().split()))
for i in range(N-1):
    if d[i] >= H:
        print(i+1)
        exit()
    else:
        d[i+1] += d[i]
if d[-1] < H: print(-1)
else: print(N)