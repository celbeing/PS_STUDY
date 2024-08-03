import sys
input = sys.stdin.readline
N = int(input())
Z = list(map(int,input().split()))
res = 0
for i in range(N):
    for j in range(i+1,N):
        res += Z[i]*Z[j]
print(res)