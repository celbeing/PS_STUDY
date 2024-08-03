#13900: 순서쌍의 곱의 합
import sys
input = sys.stdin.readline
N = int(input())
Z = list(map(int,input().split()))
pre = Z[:]
for i in range(1,N-1): pre[i] += pre[i-1]
res = 0
for i in range(N-1,0,-1):
    res += pre[i-1]*Z[i]
print(res)