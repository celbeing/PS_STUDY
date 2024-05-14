import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = list(map(int,input().split()))
days = 0
stress = 0
for k in A:
    stress += k
    if stress >= M:
        days += 1
    elif stress < 0:
        stress = 0
print(days)