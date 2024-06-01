import sys
input = sys.stdin.readline

N,M = map(int,input().split())
A = list(map(int,input().split()))
sum = [0]*M
for _ in range(N):
    ate = list(map(int,input().split()))
    for i in range(M):
        sum[i] += ate[i]
goal = True
for t in range(M):
    if sum[t] < A[t]:
        goal = False
        break
if goal: print("Yes")
else: print("No")